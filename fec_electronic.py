u"""
Driver to load, cache, parse the fec filings
uses the new Fech module which is being ported from ruby
"""

#ftp://ftp.fec.gov/FEC/electronic/20130718.zip

import cache
import zipcsv
import fech
#import fech_rendered_maps

BASEURL = 'ftp://ftp.fec.gov/FEC/electronic/'
def listing():
    u"""
    execute the listing
    """
    dirlisting = cache.cacheweb('ftp://ftp.fec.gov/FEC/electronic/')
    for filename in dirlisting.split():
        print("consider file %s" % filename)
        if (filename.find(".zip") >0 ):
            print("going to get file %s" % BASEURL + filename)
            cached_file = cache.cachewebfile(BASEURL + filename)
            print("cached file %s" % cached_file)
            csv_data = zipcsv.ZipCSV()
#            parser = fech_rendered_maps.FieldParser()
            parser = fech.Parser()

            parser.set_zipfilename(filename)

            csv_data.process_generate (
                cached_file,
                "FecElectronicFilings",
                parser)

listing()


