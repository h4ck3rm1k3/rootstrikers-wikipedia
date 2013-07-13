import secret
import httplib, urllib, base64 
import cache
import time
import re
def fetch(name): 
    params = urllib.urlencode({ 
        'key': secret.washpo(),   
        'variant': name,
        'resource_type': 'entity',
        'resource_subtype': 'person'})
    try:
        print  "searching",name
        headers = {}

        tries = 10
        while (tries > 0) :
            conn = httplib.HTTPConnection('api.washingtonpost.com')
            conn.request("GET", "/trove/v1/resources?%s" % params, "", headers)
            response = conn.getresponse()
            data = response.read()        
            conn.close()

            match = re.search("Try again in (\d+) sec",data)   
            if (match):
                s=int(match.group(1))
                time.sleep(s + 1)
                tries = tries -1 
            else:
                print "OK",data
                time.sleep(5)
                return data

    except Exception as e:
        print e
        return None

def trove(name) :
    headers = {}
    key= "wp_" + name 
    print key
    f=lambda : fetch(name)
    cache.cache(key,f)

