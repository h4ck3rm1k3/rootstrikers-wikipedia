import os
import legislators_current as leg
import cache 
import urllib
import encode
import re 
from cStringIO import StringIO
import pprint

_legs=None
_glob=None

"""

this will index the phone numbers and websites to find the legislators
we can use that to look for links in the washpost pages by url or phone.

"""

def index(contacts,n,term,target_field,field_list):
    for field_name in field_list :
        if field_name in term :
            if target_field not in contacts:
                contacts[target_field]={}
            v=term[field_name]
            v = v.rstrip("/")
            if v in contacts[target_field]:
                n2=contacts[target_field][v]
                if not n == n2 :
                    #print "error",v,n,n2,field_name,target_field
                    pass
            else:
                contacts[target_field][v]=n
         

def process():            
    global _legs
    contacts={}
    for x in sorted(_legs['wp'].keys()):
        for t in _legs['wp'][x]['terms']:
            index(contacts,x,t,'url',['contact_form','url'])
            index(contacts,x,t,'phone',['phone','fax'] )
    return contacts


def lookup(target_field,val):
    global _legs
    global _glob
    if val in _glob[target_field]:
        name=_glob[target_field][val]
        if "found" in _legs['wp'][name]:
            _legs['wp'][name]["found"] = _legs['wp'][name]["found"] + 1
        else:
            _legs['wp'][name]["found"] = 1

        return name

    return None


def report():            
    global _glob
    global _legs
    if _legs is None :
        print "No Legs"
        return

    for x in sorted(_legs['wp'].keys()):
        if "found" not in _legs['wp'][x]:
            print "missing",x
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(_glob)

def loadlegs():
    return leg.load()

def doit():
    return process()
_legs=cache.cache("legs",loadlegs)
_glob=cache.cache("contact_index",doit)
       

#print 
