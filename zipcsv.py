import zipfile
import os 
import re

class Parser :
    
    def endHeader(self):
        print "END HEADER"

    def HDR(self,l):
        print "HEADER LINE", l.split(",")

class ZipCSV :
    def process_csv (self,filename):
        zfile = zipfile.ZipFile(filename)
        for name in zfile.namelist():
            (dirname, filename) = os.path.split(name)
            print "reading " + filename + " on " + dirname
            d=zfile.read(name)
            for l in d.split("\n"):
                self.process(l)
    def process_generate (self,filename,classname):
        h = Parser()

        zfile = zipfile.ZipFile(filename)
        for name in zfile.namelist():
            (dirname, filename) = os.path.split(name)
            print "reading " + filename + " on " + dirname
            d=zfile.read(name)
           
            for l in d.split("\n"):
                if re.match(r'\/\* End Header',l):
                    h.endHeader()
                    return

                if re.match(r'HDR',l):
                    h.HDR(l)
                    return
#                print l
#                v=l.split("")
                
#                self.generate(v,classname)
#                return
    def generate(self,v,name):
        c=0
#        print "class %s:"  % name
        v2=[]
        v3=[]
        for f in v :
            f=f.strip(" ").rstrip(" ")
            f=f.strip("\"").rstrip("\"")
            #self.fields_dict[f]=c
            print "    %s=%d" % (f,c)
#            print "    def get%s(self):\n        return self.v[%s.%s]" % (f,name,f)
            
            c=c+1
#            v2.append(f)       
#            v3.append("r.get%s()" % (f)) 
#        print "    fields=%s" % (v2)
#        print "    def printall(self):\n        print %s" % (",".join(v3))
