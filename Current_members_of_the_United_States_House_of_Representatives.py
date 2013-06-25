
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
            match= re.search("http:\/\/bioguide.congress.gov\/scripts\/biodisplay\.pl\?index\=(.*)$", f_link)
            if (match):
                congbio = match.group(1).upper()
                obj['links']['congbio']=congbio #= f_link
            if (re.search("http:.*gov/$", f_link)):
                """ based on the link, point to the object, we should be able to merge data sets based on the homepage """ 
                obj['links']['homepage'][f_link]= obj
                #print "gov:" + f_link
    return obj

def parse_wiki_page(x,reps,obj) :
    d = cache.cachewp ('http://en.wikipedia.org%s?printable=yes' % x)
    html = lxml.html.document_fromstring(
        d
    )
    return parse_wiki_page_links(html,reps,obj)
    
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
                'links' :   {
                    'congbio' : '',
                    'homepage' : {}
                },
                'link' :   f_name_link,
                'district' :  f_district_link,
                'name' : f_name_element
            }
            link = re.search("/([^\/]+)$",f_name_link).group(1)          
            link = urllib.unquote(link)
            link = encode.decode(link)

            """ we are going to collect all the links and point to the object """ 
            reps['wp'][link]= parse_wiki_page(f_name_link,reps,obj)
            reps['names'][f_name_element]= obj

    return reps


