import os
#import legislators_current as leg
import legislators_other as leg
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
delete_data=False

"""
this will index the phone numbers and websites to find the legislators
we can use that to look for links in the washpost pages by url or phone.
"""

seen={} 

import lxml.html
def scan_contact(data, base_url) :

    try :
        d = lxml.html.document_fromstring( data   )
        d.make_links_absolute(base_url)
        for (f_name_element, attr , f_link, pos) in d.iterlinks():
            f_link= f_link.lower()
            if(attr == 'href'):
                if f_link.find("email-me") > 0:
                    print "found email",(f_name_element, attr , f_link, pos)
                    return f_link
                if f_link.find("email") > 0:
                    print "found email2",(f_name_element, attr , f_link, pos)
                    return f_link
                if f_link.find("contact") > 0:
                    print "found email4",(f_name_element, attr , f_link, pos)
                    return f_link

    except Exception, e:
        print e, "cannot read" , base_url
        return None

def scan_rss(data, base_url) :
    try :
        d = lxml.html.document_fromstring( data   )
        d.make_links_absolute(base_url)
        for (f_name_element, attr , f_link, pos) in d.iterlinks():
            f_link=f_link.lower()
            if(attr == 'href'):
                if f_link.lower().find("rss") > 0:
                    print "found rss", f_link
                    return f_link

    except Exception, e:
        print "rss error",e, "cannot read" , base_url
        return None

def index(contacts,n,term,field_list):
    global seen 
    main = cache.cacheweb (term['url'])
    for f in field_list :
        if f in term :
            url= term[f]
        else:
            newdata = ""
            print f, " missing in ",n, term
            if f == 'contact_form':
                newdata=scan_contact(main,term['url'])
            if f == 'rss_url':
                newdata=scan_rss(main,term['url'])
            if newdata is not None:
                    newdata=newdata.replace("&","&amp;")
                    term[f]=newdata

    return term 

def process():            
    global _legs
    contacts={}
    for x in sorted(_legs['wp'].keys()):
        t = _legs['wp'][x]['terms'][-1]
        t = index(contacts,x,t,['contact_form'])
        # t=index(contacts,x,t,['url'])
        t=index(contacts,x,t,['rss_url'])


    return contacts


def loadlegs():
    return leg.load()

def doit():
    return process()

_legs=loadlegs()

def save():
    dump.dump(_legs)

doit()
save()
