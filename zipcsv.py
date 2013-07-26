import zipfile
import os 
import re


class ZipCSV :
    def process_csv (self,filename):
        zfile = zipfile.ZipFile(filename)
        for name in zfile.namelist():
            (dirname, filename) = os.path.split(name)
            print "reading " + filename + " on " + dirname
            d=zfile.read(name)
            for l in d.split("\n"):
                self.process(l)

    def process_generate (self,filename,classname,parser):
#        h = Parser()

        zfile = zipfile.ZipFile(filename)
        for name in zfile.namelist():
            (dirname, filename) = os.path.split(name)
            print "reading " + filename + " on " + dirname
            d=zfile.read(name)
            parser.parse_file_data(d)

