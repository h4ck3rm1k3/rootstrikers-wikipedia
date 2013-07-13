import re
import mechanize
import cache
import codecs
import os 
import lxml.etree
import washpost
import time 
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
    print "filename", filename
    return data

for i in range(1,100):
    offset = i * 10
    filename = "data/wp_%d" % offset
    data=None
    if (os.path.exists(filename)):
        data=fetch(offset)
    else:
        f = codecs.open(filename, "rb", "utf-8")
        data= f.read()

    #<a href="http://www.washingtonpost.com/politics/randy-weber/407de97a-4bbd-11e2-8758-b64a2997a921_topic.html" rel="http://www.washingtonpost.com/politics/randy-weber/407de97a-4bbd-11e2-8758-b64a2997a921_topic.html">Randy Weber (R-Texas)</a>
    myparser = lxml.etree.HTMLParser(encoding="utf-8")
    html = lxml.etree.HTML(data, parser=myparser)
    for r in html.xpath("//h3") :
        for l in r.xpath("a"):
            f_name_link = l.get("href")

            contents= cache.cacheweb(f_name_link)

            f_name = l.text.strip()
            match = re.search("([\w\.\s]+)\((\w)\-([\w\.]+)\)$",f_name)   
            if (match):
                (name,party,state)=(match.group(1),match.group(2),match.group(3))
            else:
                (name,party,state)=("no name","no party","state")
            name = name.strip()
            name = name.rstrip()
#            if (match):
#                print "name",match.group(1),":",match.group(2),":",match.group(3)
            
            link = None 
            match = re.search("\/politics\/([\w\-]+)\/([\w\-^_]+)_topic\.html$",f_name_link)
            if (match):
                link = match.group(1)
                link2 = match.group(2)
            print "link",link,link2,"name",name,"party",party,"state",state,"raw",f_name_link
            washpost.trove(name)

