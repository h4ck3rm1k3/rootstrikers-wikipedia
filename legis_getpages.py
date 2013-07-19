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

seen={} 

def index(contacts,n,term,target_field,field_list):
    global seen 
    for f in field_list :
        if f in term :
            url= term[f]

            if url in seen:
                continue
 
            try:
                d = cache.cacheweb (url)
            except Exception, e:
                print e, url
                seen[url]=1
                d = cache.cacheweb ("http://web.archive.org/web/*/" + url)

def process():            
    global _legs
    contacts={}
    for x in sorted(_legs['wp'].keys()):
        for t in _legs['wp'][x]['terms']:
            index(contacts,x,t,'url',['contact_form','url'])

    return contacts


def loadlegs():
    return leg.load()

def doit():
    return process()

_legs=cache.cache("legs",loadlegs)

doit();

def save():
    dump.dump(_legs)
