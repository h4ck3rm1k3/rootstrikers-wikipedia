import lxml.html
import urllib2
import os

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

def parse_wiki_page(x) :
    d = cache ('http://en.wikipedia.org%s?printable=yes' % x)
    html = lxml.html.document_fromstring(
        d
    )
    
def parse_rep() :
    reps = {}
#    d = cache ('http://en.wikipedia.org/wiki/Current_members_of_the_United_States_House_of_Representatives?printable=yes')
    d = cache ('http://en.wikipedia.org/wiki/Current_members_of_the_United_States_House_of_Representatives?printable=yes')
    html = lxml.html.document_fromstring(
        d
        #    "http://en.wikipedia.org/w/index.php?title=List_of_current_United_States_Senators&printable=yes"
    )

    tables = html.xpath("//table")
    table = tables[1]
    for r in table.xpath("//tr") :
        data= r.xpath("td")
        if( len(data) == 10):
            f_district = data[1]
            f_image     = data[2]
            f_name     = data[3]

            (skip, skip , f_district_link, skip) =f_district.iterlinks().next()
#            print f_district_element, f_district_link
            (f_name_element, skip , f_name_link, skip) =f_name.iterlinks().next()
#            print "ele:%s" %  f_name_element.text
#            print "http://en.wikipedia.org" + f_name_link
            reps[f_name_element.text]= {
                'link' :   f_name_link,
                'district' :  f_district_link
            }
            parse_wiki_page(f_name_link)

    return reps

#parse_rep()
