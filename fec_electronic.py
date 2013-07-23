#ftp://ftp.fec.gov/FEC/electronic/20130718.zip

import cache

def get(url, name):
    return cache.cacheweb(url)

def listing():
    l= cache.cacheweb('ftp://ftp.fec.gov/FEC/electronic/')
    for f in l.split():
        if (f.find(".zip") >0 ):
            d= cache.cacheweb('ftp://ftp.fec.gov/FEC/electronic/' + f)

l = listing()
#print l 

