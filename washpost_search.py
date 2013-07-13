import re
import mechanize
import cache
import codecs
import os 
import lxml.etree
import washpost
import time 
import lxml.html
import legis_index_links

url='http://www.washingtonpost.com/newssearch/search.html'
br = mechanize.Browser()
br.open(url)

def fetch(offset):
    req= { 
        'startat':	str(offset),
        'query':	"house of representatives",
        'offset':	str(offset),
        'filter':	'contenttype:"Topic"',
        'facetfields':	'contenttype',
           # 'date-filter':	'displaydatetime:[2005-01-01T00:00:00Z TO NOW/DAY+1DAY]'
    } 
    forms=[]
    for form in br.forms() :
        forms.append(form)
        #print " form name", form.name

    form= forms[0]
#    print form
    if form is not None :
        form.set_all_readonly(False)
        #for x in form.controls :
        #    
        for k in req.keys():
            #print "key", k
            v=req[k]
            #print "val",v
            form[k]=v
    r = form.click()
    request2 = form.click()  # mechanize.Request object
    try:
        response2 = mechanize.urlopen(request2)
    except mechanize.HTTPError, response2:
        pass

    data= response2.read()  # body
    response2.close()

    filename = "data/wp_%d" % offset
    data = data.decode("utf-8")
    f = codecs.open(filename,'wb','utf-8')
    f.write(data)
    #print "filename", filename
    return data

def xlinks (page):
    links={}
#    myparser = lxml.etree.HTMLParser(encoding="utf-8")
#    html = lxml.etree.HTML(page, parser=myparser)
    html = lxml.html.document_fromstring( page )
    for (f_name_element, attr , f_link, pos) in html.iterlinks():
        #if(attr == 'href'):
        #    for r in html.xpath("//a") :
        #        f_link = l.get("href")

        links[f_link]=1
        if f_link.find("washingtonpost")> 0 :
            continue

        if f_link.find("washpost")> 0 :
            continue

        if f_link.find("mailto")>= 0:
            #print "external mail",f_link,pos, attr
            continue
        if f_link.find(".gov")>= 0:

            f_link = f_link.rstrip("/")
#            wiki =legis_index_links.lookup("url",f_link)
#            if wiki is not None :
#                print "foun",wiki,f_link
#                return wiki
#            else:
#                print "external gov no match",f_link,pos, attr
            continue
        if f_link.find("wiki")>= 0:
            print "external wiki",f_link,pos, attr
    return links

def runtrove(name):
    print "run trove",name
    for x in range(1,1000):
        try :
            d= washpost.trove(name)
            print "Got",d
            return d
        except Exception, e:
            print "Er on trove", name , e
    return None


def extract_links(f_name_link):
    print "extract_links",f_name_link
    contents=""
    try :
        contents= cache.cacheweb(f_name_link)
    except :
        # try once agains
        contents= cache.cacheweb(f_name_link)
    return xlinks(contents)
    

def parse_name (f_name):
    match = re.search("([\w\.\s]+)\((\w)\-([\w\.]+)\)$",f_name)   
    if (match):
        (name,party,state)=(match.group(1),match.group(2),match.group(3))
    else:
        (name,party,state)=("no name","no party","state")
    name = name.strip()
    name = name.rstrip()
    return (name,party,state)

def parse_link (f_name_link):
    link = None 
    match = re.search("\/politics\/([\w\-]+)\/([\w\-^_]+)_topic\.html$",f_name_link)
    if (match):
        link = match.group(1)
        link2 = match.group(2)
        return (link,link2)
    else:
        return ("","")

def process_link(l):
            f_name_link = l.get("href")
            f_name = l.text.strip()

            callit = lambda : extract_links(f_name_link)
#           cache.delcache("wp"+ f_name)
            extract = cache.cache("wp"+ f_name,callit)
            (name,party,state)=parse_name (f_name)
            (link,link2) = parse_link (f_name_link)
####
            callit = lambda : runtrove(name)
#            troveid = runtrove(name)
#            cache.delcache("wpt"+ f_name)
            troveid = cache.cache("wpt"+ f_name,callit)

#            print "missing link",link,link2,"name",name,"party",party,"state",state,"raw",f_name_link


# search all the pages of results on congress members
for i in range(1,100):
    offset = i * 10
    filename = "data/wp_%d" % offset
    data=None
    if (not os.path.exists(filename)):
        data=fetch(offset)
    else:
        f = codecs.open(filename, "rb", "utf-8")
        data= f.read()

    #<a href="http://www.washingtonpost.com/politics/randy-weber/407de97a-4bbd-11e2-8758-b64a2997a921_topic.html" rel="http://www.washingtonpost.com/politics/randy-weber/407de97a-4bbd-11e2-8758-b64a2997a921_topic.html">Randy Weber (R-Texas)</a>
    myparser = lxml.etree.HTMLParser(encoding="utf-8")
    html = lxml.etree.HTML(data, parser=myparser)
    for r in html.xpath("//h3") :
        for l in r.xpath("a"):
            process_link(l)


legis_index_links.report()
