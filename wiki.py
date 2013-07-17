
import urllib2
import urllib
import os
import re
import cache
import encode
import lxml.html
import lxml
def fec (f_link,obj):
    match= re.search("http:\/\/herndon1\.sdrdc\.com\/cgi-bin\/can_detail\/(.*)$", f_link)
    if (match):
        val = match.group(1)
#        print "extract fec" 
        obj['links']['fec']=val
    

def cspan (f_link,obj):
    match= re.search("http:\/\/c-spanvideo\.org\/person\/(.*)$", f_link)
    if (match):
        val = match.group(1)
        if (re.search(val,"\d+")):
            print "cspan numeric" , val
            obj['links']['cspan']=val
        else:
            print "cspan string" , val
            obj['links']['cspan']=val            
        return
    
    match= re.search("http:\/\/c-spanvideo\.org\/(.*)$", f_link)
    if (match):
        val = match.group(1)
        print "cspan short" , val
        obj['links']['cspan']=val


def ballot (f_link,obj):
    match= re.search("http:\/\/ballotpedia\.org\/wiki\/index\.php\/(.*)$", f_link)
    if (match):
        val = match.group(1)
        obj['links']['ballot']=val

def opencongress (f_link,obj):
    match= re.search("http://www.opencongress.org/people/show/(.*)$", f_link)
    if (match):
        val = match.group(1).upper()
        obj['links']['opencong']=val

def congbio (f_link,obj):
    match= re.search("http:\/\/bioguide.congress.gov\/scripts\/biodisplay\.pl\?index\=(.*)$", f_link)
    if (match):
        val = match.group(1).upper()
        obj['links']['bioguide']=val

def votesmart (f_link,obj):
    match= re.search("http:\/\/www.votesmart.org\/candidate\/(\d+)$", f_link)
    if (match):
        val = match.group(1)
        obj['links']['votesmart']=val

def wikipedia (f_link,obj):
                     #http:\/\/en\.wikipedia\.org\/wiki\/Aaron_Schock
    match= re.search("http:\/\/en\.wikipedia\.org\/wiki\/(.+)$", f_link)
    if (match):
        val = match.group(1)
        obj['links']['wikipedia']=val

def govhomepage(f_link,obj):
    if (re.search("http:.*gov/$", f_link)):
        """ based on the link, point to the object, we should be able to merge data sets based on the homepage """ 
        obj['links']['homepage'][f_link]= obj

def parse_wiki_page_links(d,reps,obj):
    for (f_name_element, attr , f_link, pos) in d.iterlinks():
        if(attr == 'href'):
            opencongress(f_link,obj)
            ballot(f_link,obj)
            congbio(f_link,obj)
            votesmart(f_link,obj)
            govhomepage(f_link,obj)
            wikipedia(f_link,obj)
            cspan(f_link,obj)
            fec(f_link,obj)
    return obj

def parse_wiki_page(x,reps,obj):
    d = cache.cachewp ('http://en.wikipedia.org%s?action=purge&printable=yes' % x)
    html = lxml.html.document_fromstring( d   )
    return parse_wiki_page_links(html,reps,obj)

def parse_wiki_text(d,reps) :
    match= re.search("{{CongLinks(.+)}}", d)
    d = {}
    if (match):
        val = match.group(1)
        val = val.replace("&newMem=Y","")
        val = val.replace("&newmem=Y","")
        for x in val.split("|"):
            try :
                if (x.find("=") > 0):
                    (k,v) = x.split("=")
                    k = k.replace(" ","")
                    k = k.replace("\'","")
                    v=v.strip(" ")
                    v=v.rstrip(" ")
                    v=v.strip("'")
                    v=v.rstrip("'")

#                    if (k == 'opensecrets') :
#                        print "Cong" ,x,"\'%s\'" % k,v
                    d[k]=v
            except Exception,e :
                print "error1",x, e, val
        d["raw"]= val
    return d 
    
def parse_wiki_source(x,reps):
    url='http://en.wikipedia.org/w/index.php?title=%s&action=raw' % x
    d = cache.cachewp (url)
    return parse_wiki_text(d,reps)

