#!/usr/bin/python
import os
#import socrata_rows as soc
import Current_members_of_the_United_States_House_of_Representatives as reps
import List_of_current_United_States_Senators as sens
import cache 
import legislators_current as leg

from cStringIO import StringIO

rep= cache.cache('reps',reps.parse_rep)
#rep= reps.parse_rep()
sen= cache.cache('sen',sens.parse)

congress = { 'wp' : rep['wp'].copy() }
congress['wp'].update(sen['wp'])
legs= leg.load()

#print "REPS:",sorted(rep['wp'].keys())
#print "SEN:",sorted(sen['wp'].keys())
#print "TOTAL:",sorted(congress['wp'].keys())
#print "Legs:",sorted(legs['wp'].keys())

def check(aobj,bobj,name):

    if name in bobj['id'] :
        bval= str(bobj['id'][name])
        if name in aobj['links'] :
            aval = str(aobj['links'][name])
            if aval != bval :
#                print "aval " ,aval
                print "Found " , name,  aval, "/", bval

#        else:
#            print 'in a no :' + name , aobj['links']
    else:
        if name in aobj['links'] :
            val = str(aobj['links'][name])
            print 'in b no ' + name ,  "IN A: ", name + ": " + val, bobj['id']
            bobj['id'][name]=val
        else:
            print 'in b no ' + name ,   "not in a",bobj['id']


def compare(a,b) :

    for x in sorted(a['wp'].keys()):
        aobj = a['wp'][x]
        if x in b['wp'] :
            bobj = b['wp'][x]

            if 'links' in aobj :
                check(aobj,bobj,'bioguide')               
                check(aobj,bobj,'votesmart')
                check(aobj,bobj,'ballot')
            else:
                print 'no links' 
                print aobj                
        else:
            print "Missing %s " % x
 #           print aobj


print "Wikipedia\n"
#print congress
compare(congress,legs)
#print "Legs\n"
#compare(legs,congress)
# for x in sorted(legs['wp'].keys()):
#     if 'bioguide' not in legs['wp'][x]['id']:
#         print  " missing bioguide " + x 

#     if 'votesmart' not in legs['wp'][x]['id']:
#         print  " missing votesmart " + x 
import yaml
out = open("dump.yaml", 'w')

import re

try:
    from yaml import CSafeLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import SafeLoader as Loader, Dumper
from collections import OrderedDict

def construct_odict(load, node):
    omap = OrderedDict()
    yield omap
    if not isinstance(node, yaml.MappingNode):
        raise yaml.constructor.ConstructorError(
            "while constructing an ordered map",
            node.start_mark,
            "expected a map, but found %s" % node.id, node.start_mark
        )
    for key, value in node.value:
        key = load.construct_object(key)
        value = load.construct_object(value)
        omap[key] = value

Loader.add_constructor(u'tag:yaml.org,2002:map', construct_odict)
def ordered_dict_serializer(self, data):
    return self.represent_mapping('tag:yaml.org,2002:map', data.items())
Dumper.add_representer(OrderedDict, ordered_dict_serializer)

# Likewise, when we store unicode objects make sure we don't write
# them with weird YAML tags indicating the Python data type. The
# standard string type is fine. We should do this:
# Dumper.add_representer(unicode, lambda dumper, value: dumper.represent_scalar(u'tag:yaml.org,2002:str', value))
#
# However, the standard PyYAML representer for strings does something
# weird: if a value cannot be parsed as an integer quotes are omitted.
#
# This is incredibly odd when the value is an integer with a leading
# zero. These values are typically parsed as octal integers, meaning
# quotes would normally be required (that's good). But when the value
# has an '8' or '9' in it, this would make it an invalid octal number
# and so quotes would no longer be required (that's confusing).
# We will override str and unicode output to choose the quotation
# style with our own logic. (According to PyYAML, style can be one of
# the empty string, ', ", |, or >, or None to, presumably, choose
# automatically.
def our_string_representer(dumper, value):
# If it looks like an octal number, force '-quote style.
    style = None
    if re.match(r"^0\d*$", value): style = "'"
    return dumper.represent_scalar(u'tag:yaml.org,2002:str', value, style=style)
Dumper.add_representer(str, our_string_representer)
Dumper.add_representer(unicode, our_string_representer)

# Add a representer for nulls too. YAML accepts "~" for None, but the
# default output converts that to "null".
Dumper.add_representer(type(None), lambda dumper, value : \
dumper.represent_scalar(u'tag:yaml.org,2002:null', u"~"))

leg.apply(legs)
yaml.dump(legs['raw'], out,  default_flow_style=False, allow_unicode=True, Dumper=Dumper)
