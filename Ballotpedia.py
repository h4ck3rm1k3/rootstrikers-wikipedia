import urllib2
import urllib
import os
import re
import cache
import encode
import lxml.html
import lxml
import wiki

""" 
the results is a dictionary :
names
links
wp

""" 

def parse_ballotwiki_page(x,reps,obj) :
    d = cache.cachewp ('http://ballotpedia.org%s?printable=yes' % x)
    html = lxml.html.document_fromstring( d   )
    return wiki.parse_wiki_page_links(html,reps,obj)
    
def parse(url) :
    reps = {
    'wp': {},
    'names': {},
    'links': {},
    }
    d = cache.cachewp (url)
    myparser = lxml.etree.HTMLParser(encoding="utf-8")
    html = lxml.etree.HTML(d, parser=myparser)
    for r in html.xpath("//ol/li") :
        for l in r.xpath("a"):
            f_name_link = l.get("href")
            f_name_element = l.text

            obj = {
                'links' :   {
                    'homepage' : {}
                },
                'link' :   f_name_link,
                'name' : f_name_element
            }
            link = re.search("/([^\/]+)$",f_name_link).group(1)          
            link = urllib.unquote(link)
            link = encode.decode(link)

            """ we are going to collect all the links and point to the object """ 
#            print link, f_name_element,  f_name_link 
            reps['wp'][link]= parse_ballotwiki_page(f_name_link,reps,obj)
            reps['names'][f_name_element]= obj

    return reps


