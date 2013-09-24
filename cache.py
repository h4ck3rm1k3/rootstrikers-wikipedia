import os
import pickle
import re
import urllib2
#import urllib
import codecs
#verbose = False
verbose = True

def doload(x,f):
    filename = "data/%s.pkl" % x
    output = open(filename, 'wb')
    data = f()
    if data is None :
        raise Exception (" ".join(["for",x,"for", filename,"got None"]))
    s= str(data)
    l =len(s)
    if (l > 80 ):
        l=80
    print "for",x,"for", filename,"got",s[:l]
    pickle.dump(data, output)
    return data

def delcache(x) :
    filename = "data/%s.pkl" % x
    if (os.path.exists(filename)):
        os.remove(filename)

def cache (x,f) :

    filename = "data/%s.pkl" % x

    if not os.path.exists("data"):
        os.makedirs("data")
    if (os.path.exists(filename)):
        pkl_file = open(filename, 'rb')
        try :
            data = pickle.load(pkl_file)
            return data
        except :
            # just load it
            return doload(x,f)

    else:
        return doload(x,f)


def cachewp (url) :
    data = cacheweb(url)
    if (re.search("Redirected from",data)):
        raise Exception( " redirect %s" % url)
        #print "redirect %s" % url
    return data


def cachewebfile (url) :
    url2=url
    url2=url2.replace("/","_")
    filename = "data/" + url2
    filename = filename.replace('action=purge&','')

    if not os.path.exists("data"):
        os.makedirs("data")

    if (os.path.exists(filename)):
        if verbose :
            #print "get url" , url, " from file ", filename
            return filename

    ###
#    if verbose :
#        print "get", url
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cache-Control' : 'no-cache, no-store, max-age=0, must-revalidate',
        'Pragma' : 'no-cache',
#        'Accept-Charset': 'utf-8',
#        'Accept-Language': 'en-US',
        'Connection': 'keep-alive'
    }

    r = urllib2.Request(url=url, headers=hdr     )
    d=None
    try:
        d = urllib2.urlopen(r)
    except urllib2.HTTPError, e:
        print "error http",e
        raise e 
    except Exception, e: 
        print "other",e
        raise e 
    except:
        print "could not load "
        exit()
    
    data= d.read()
    try :
        data2 = data.decode("utf-8")
        f = codecs.open(filename,'wb','utf-8')
        f.write(data2)
        f.close()
        print "write", filename
        return filename
    except Exception, e :
        print "error decoding", e
        
        try :
            f = open(filename,'wb')
            f.write(data)
            f.close()
            return filename
        except Exception, e :
            print "decoding2", e
    
    return None

def cacheweb (url) :

    filename =cachewebfile (url)
    if (os.path.exists(filename)):
        if verbose :
            #print "get url" , url, " from file ", filename
            pass
        try:
            f = codecs.open(filename, "rb", "utf-8")
            data= f.read()
            return data
        except Exception,e :
            print "failed to open, ", e, "try again without utf8"
            f = open(filename, "rb")
            data= f.read()
            return data

    return None

import pycurl
import StringIO
    
def curlget(url):
    c = pycurl.Curl()
    c.setopt(pycurl.URL, url)
    print " pycurl", url
    b = StringIO.StringIO()
    c.perform()
    c.close()
    data = b.getvalue()
    return data

