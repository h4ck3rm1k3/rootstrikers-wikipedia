
import urllib2
import urllib
import os
import re
import cache
import encode
import lxml.html
import lxml

def congbio (f_link,obj):
    match= re.search("http:\/\/bioguide.congress.gov\/scripts\/biodisplay\.pl\?index\=(.*)$", f_link)
    if (match):
        congbio = match.group(1).upper()
        obj['links']['bioguide']=congbio #= f_link

def votesmart (f_link,obj):
    match= re.search("http:\/\/www.votesmart.org\/candidate\/(\d+)$", f_link)
    if (match):
        val = match.group(1)
        obj['links']['votesmart']=val
#        print val

def govhomepage(f_link,obj):
    if (re.search("http:.*gov/$", f_link)):
        """ based on the link, point to the object, we should be able to merge data sets based on the homepage """ 
        obj['links']['homepage'][f_link]= obj

def parse_wiki_page_links(d,reps,obj):
    for (f_name_element, attr , f_link, pos) in d.iterlinks():
        if(attr == 'href'):
            congbio(f_link,obj)
            votesmart(f_link,obj)
            govhomepage(f_link,obj)
    return obj

def parse_wiki_page(x,reps,obj) :
    d = cache.cachewp ('http://en.wikipedia.org%s?printable=yes' % x)
    html = lxml.html.document_fromstring( d   )
    return parse_wiki_page_links(html,reps,obj)

