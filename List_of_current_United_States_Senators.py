import lxml.html
import urllib2
import urllib
import os
import re
import cache
import encode 
import wiki

# List_of_current_United_States_Senators
""" 
the results is a dictionary :
names
links
wp
""" 
   
def parse() :
    reps = {
    'wp': {},
    'names': {},
    'links': {},
    }
    d = cache.cachewp ('http://en.wikipedia.org/wiki/List_of_current_United_States_Senators?printable=yes')
    html = lxml.html.document_fromstring(  d  )
    tables = html.xpath("//table")
    table = tables[1]
    for r in table.xpath("//tr") :
        data= r.xpath("td")
        if( len(data) > 7):
            f_state = data[1]
            f_class = data[2]
            f_image = data[3]
            f_name  = data[4]

            (f_name_element, skip , f_name_link, skip) =f_name.iterlinks().next()
            obj = {
                'type': 'senate',
                'links' :   {
#                    'congbio' : '',
                    'homepage' : {}
                },
                'link' :   f_name_link,
                'state' :   f_state.text,
                'district' :  f_class.text,
                'name' : f_name_element.text
            }


            link = re.search("/([^\/]+)$",f_name_link).group(1)          
            link = urllib.unquote(link)
            link = encode.decode(link)

            """ we are going to collect all the links and point to the object """ 
            obj=wiki.parse_wiki_page(f_name_link,reps,obj)
            reps['wp'][link]= obj
            reps['names'][f_name_element.text]= obj

    return reps


