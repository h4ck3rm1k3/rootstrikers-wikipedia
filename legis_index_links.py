import os
import legislators_current as leg
import cache 
import urllib
import encode
import re 
from cStringIO import StringIO
import pprint
from urlparse import urlunsplit,urlsplit
import dump
_legs=None
_glob=None
import json 

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

def lookup(target_field,val,name,party,state,link,link2,troveid):
    global _legs
    global _glob

    o = urlsplit(val)
    o0= o[0]
    if o0=="https":
        o0="http"
    
    v2 = urlunsplit([o0,o[1],"","",""])
    v2 = v2.strip()
    v2 = v2.rstrip()

    if v2.find('.gov') < 0:
        return None 

    if v2 == 'http://www.washingtonpost.com':
        return None 

    if v2 == '':
        return None 

    if v2 in _glob[target_field]:
        name=_glob[target_field][v2]
#        if "found" in _legs['wp'][name]:
#            _legs['wp'][name]["found"] = _legs['wp'][name]["found"] + 1
#        else:
#             _legs['wp'][name]["found"] = 1

        #print "found ",v2,name
#        _legs['wp'][name]['id']['washpost_name']=name
        _legs['wp'][name]['id']['washpo']=link2
#        _legs['wp'][name]['id']['washpost_link2']=link2
        tid=0
        try :
            trove = json.loads(troveid)
            if "resources" in trove:
                tid=trove["resources"]['id']
        except :
            pass


        _legs['wp'][name]['id']['washpost_troveid']=tid

        return name
#    print "not found ",v2
    return None

def strip(data):
    data2={}
    for v in data["url"]:
        w=data["url"][v]
        o = urlsplit(v)
        v2 = urlunsplit([o[0],o[1],"","",""])
#        print o,v,v2
        data2[v2]=w
    for x in data2.keys():
        data["url"][x]=data2[x]
    return data


def report():            
    global _glob
    global _legs
    if _legs is None :
        print "No Legs"
        return
#    for x in sorted(_legs['wp'].keys()):
#        if "found" not in _legs['wp'][x]:
#            print "missing",x
#        else:
#            print "found",x
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(_glob)
    save()

def loadlegs():
    return leg.load()

def doit():
    return process()

_legs=cache.cache("legs",loadlegs)
_glob=cache.cache("contact_index",doit)
_glob=strip(_glob)

def save():
    dump.dump(_legs)
