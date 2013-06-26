import yaml
import cache
import encode
import codecs

from yaml import CSafeLoader as Loader, CDumper as Dumper
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

def loadlegis ():
    filename ='congress-legislators/legislators-current.yaml'
    f = codecs.open(filename, "rb", "utf-8")
    data = f.read()
    legis = yaml.load(data,Loader=Loader)
    return legis

def load():
    legis = cache.cache ( "legis",loadlegis)
    data = {  'wp' : {},       'raw' : legis    }
    for l in legis:
        if 'wikipedia' in l['id'] :
            wp = l['id']['wikipedia']
            wp = wp.replace(" ","_")
            wp = encode.decodeuc(wp)
            data['wp'][wp]=l
        else:
            print  "no wikipedia ", l 
    return data


def apply(data):
    for l in data['raw'] :
        if 'wikipedia' in l['id'] :
            wp = l['id']['wikipedia']
            wp = wp.replace(" ","_")
            wp = encode.decodeuc(wp)
            new = data['wp'][wp]
            l['id']=new['id']
#            if ('ballot' in new['id']) :

# clean up the ballot
            if 'ballot' in l['id']: 
                b = l['id']['ballot']
                del l['id']['ballot']
                b=b.replace("_"," ")
                l['id']['ballotpedia']=b

    return data
