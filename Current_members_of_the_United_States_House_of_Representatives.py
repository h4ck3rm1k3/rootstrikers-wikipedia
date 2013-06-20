import lxml.html
import urllib2
import os
import re

""" 
the results is a dictionary :
names
links

""" 

def cache (url) :
    print url
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    url2=url
    url2=url2.replace("/","_")
    filename = "data/" + url2

    if not os.path.exists("data"):
        os.makedirs("data")

    if (os.path.exists(filename)):
        f =open(filename,'r')
        return f.read()
    else:
        r = urllib2.Request(url=url, headers=hdr     )
        d = urllib2.urlopen(r)
        data= d.read()
        f =open(filename,'w')
        f.write(data)
        return data



def parse_wiki_page_links(d,reps,obj):
    for (f_name_element, attr , f_link, pos) in d.iterlinks():
        if(attr == 'href'):
            if (re.search("http:.*gov/$", f_link)):
                """ based on the link, point to the object, we should be able to merge data sets based on the homepage """ 
                reps['links'][f_link]= obj
                #print "gov:" + f_link

def parse_wiki_page(x,reps,obj) :
    d = cache ('http://en.wikipedia.org%s?printable=yes' % x)
    html = lxml.html.document_fromstring(
        d
    )
    parse_wiki_page_links(html,reps,obj)
    
def parse_rep() :
    reps = {
    'names': {},
    'links': {},
    }
    d = cache ('http://en.wikipedia.org/wiki/Current_members_of_the_United_States_House_of_Representatives?printable=yes')
    html = lxml.html.document_fromstring(  d  )
    tables = html.xpath("//table")
    table = tables[1]
    for r in table.xpath("//tr") :
        data= r.xpath("td")
        if( len(data) == 10):
            f_district = data[1]
            f_image     = data[2]
            f_name     = data[3]
            (skip, skip , f_district_link, skip) =f_district.iterlinks().next()
            (f_name_element, skip , f_name_link, skip) =f_name.iterlinks().next()
            obj = {
                'link' :   f_name_link,
                'district' :  f_district_link,
                'name' : f_name_element.text
            }
            reps['names'][f_name_element.text]= obj
            """ we are going to collect all the links and point to the object """ 
            parse_wiki_page(f_name_link,reps,obj)

    return reps


