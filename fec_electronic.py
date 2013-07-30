#ftp://ftp.fec.gov/FEC/electronic/20130718.zip

import cache
import zipcsv
import Fech
import Fech_rendered_maps

#def get(url, name):
#    return cache.cachewebfile(url)

def listing():
    l= cache.cacheweb('ftp://ftp.fec.gov/FEC/electronic/')
    for f in l.split():
        if (f.find(".zip") >0 ):
            f= cache.cachewebfile('ftp://ftp.fec.gov/FEC/electronic/' + f)
            print f
            e1=zipcsv.ZipCSV()
            parser=Fech_rendered_maps.FieldParser()
            e1.process_generate (f,"FecElectronicFilings",parser)

l = listing()
#print l 

