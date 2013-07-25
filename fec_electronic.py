#ftp://ftp.fec.gov/FEC/electronic/20130718.zip

import cache
import zipcsv
#def get(url, name):
#    return cache.cachewebfile(url)

def listing():
    l= cache.cacheweb('ftp://ftp.fec.gov/FEC/electronic/')
    for f in l.split():
        if (f.find(".zip") >0 ):
            f= cache.cachewebfile('ftp://ftp.fec.gov/FEC/electronic/' + f)
            print f
            e1=zipcsv.ZipCSV()
            e1.process_generate (f,"FecElectronicFilings")

l = listing()
#print l 

