import os
import pickle
import re
import urllib2
import urllib
import codecs
verbose = False

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
        raise Exception( " redirect %s" % url)
        #print "redirect %s" % url
    return data


def cacheweb (url) :
    if verbose :
        print "get", url
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cache-Control' : 'no-cache, no-store, max-age=0, must-revalidate',
        'Pragma' : 'no-cache',
        'Accept-Charset': 'utf-8',
        'Accept-Language': 'en-US',
        'Connection': 'keep-alive'
    }
    url2=url
    url2=url2.replace("/","_")
    filename = "data/" + url2
    filename = filename.replace('action=purge&','')

    if not os.path.exists("data"):
        os.makedirs("data")

    if (os.path.exists(filename)):
        if verbose :
            print "get file" + url
        f = codecs.open(filename, "rb", "utf-8")
        data= f.read()
        return data
    else:

        print "get " + url
        r = urllib2.Request(url=url, headers=hdr     )
        d = urllib2.urlopen(r)
        data= d.read()
        data = data.decode("utf-8")
        f = codecs.open(filename,'wb','utf-8')

        f.write(data)
        return data

