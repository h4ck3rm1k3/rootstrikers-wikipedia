
import urllib2
import urllib
import os
import re
import cache
import encode
import lxml.html
import lxml

""" 
the results is a dictionary :
names
links
wp

""" 

def parse_wiki_page_links(d,reps,obj):
    for (f_name_element, attr , f_link, pos) in d.iterlinks():
        if(attr == 'href'):
            if (re.search("http:.*gov/$", f_link)):
                """ based on the link, point to the object, we should be able to merge data sets based on the homepage """ 
                reps['links'][f_link]= obj
                #print "gov:" + f_link

def parse_wiki_page(x,reps,obj) :
    d = cache.cachewp ('http://en.wikipedia.org%s?printable=yes' % x)
    html = lxml.html.document_fromstring(
        d
    )
    parse_wiki_page_links(html,reps,obj)
    
def parse_rep() :
    reps = {
    'wp': {},
    'names': {},
    'links': {},
    }
    d = cache.cachewp ('http://en.wikipedia.org/wiki/Current_members_of_the_United_States_House_of_Representatives?printable=yes')

    myparser = lxml.etree.HTMLParser(encoding="utf-8")
    html = lxml.etree.HTML(d, parser=myparser)

    tables = html.xpath("//table")
    table = tables[1]
    for r in table.xpath("//tr") :
        data= r.xpath("td")
        if( len(data) == 10):
            f_district = data[1]
            f_image     = data[2]
            f_name     = data[3]
            f_name_link = ""
            f_name_element = ""
            f_district_link=""
            for l in f_name.xpath("span/span/a"):
                f_name_link = l.get("href")
                f_name_element = l.text

            for l in f_district.xpath("span/span/a"):
                f_district_link = l.get("href")

            obj = {
                'link' :   f_name_link,
                'district' :  f_district_link,
                'name' : f_name_element
            }
            reps['names'][f_name_element]= obj

            link = re.search("/([^\/]+)$",f_name_link).group(1)          
            link = urllib.unquote(link)
            link = encode.decode(link)
            reps['wp'][link]= obj

            """ we are going to collect all the links and point to the object """ 
#            parse_wiki_page(f_name_link,reps,obj)

    return reps


