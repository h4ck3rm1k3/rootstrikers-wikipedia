import os
import pickle
import re
import urllib2
import urllib

def cache (x,f) :

    filename = "data/%s.pkl" % x

    if not os.path.exists("data"):
        os.makedirs("data")
    if (os.path.exists(filename)):
        pkl_file = open(filename, 'rb')
        data = pickle.load(pkl_file)
        return data
    else:
        output = open(filename, 'wb')
        data = f()
        pickle.dump(data, output)
        return data

def cachewp (url) :
    data = cacheweb(url)
    if (re.search("Redirected from",data)):
        #raise Exception( " redirect %s" % url)
        print "redirect %s" % url
    return data


def cacheweb (url) :
#    print url
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

