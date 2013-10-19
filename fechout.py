#encapsulate the output of fec
import yaml
#from 
import os

def checkin(path,filename):
    print "going to process %s" % path
    os.system("bash ./checkin.sh %s %s" % (path,filename))

class FechoutFile ():
    u"""
    Wrapper for fech, manage the zip file
    """
    def __init__(self,name,sourcefile,baseurl, urlfile):
        self.name=name
        self.sourcefile=urlfile
        self.sourceurl= baseurl + "/" + urlfile
        self.outfile=None
        self._attr={}
        self._rows=[]
        self._raw=[]
        self.open()

    def raw_line(self,line):
        self._raw.append(line)

    def pathname(self):
        self.sourcefile = self.sourcefile.replace (".zip","")
        year = self.sourcefile[0:4]
        #print(year)
        return "fech_yaml/%s/%s/" % (year,self.sourcefile)

    def filename(self, count =0):

        self._filename =  self.name 

        if (count > 0):
            self._filename = self._filename +  "_%d" % count
                    
        self._filename = self._filename +  ".yml"

        return self._filename

    def exists(self):
        return os.path.exists(self.pathname () + self.filename())

    def open(self):
        try:
            if not os.path.exists(self.pathname()):
                os.makedirs(self.pathname())
        except Exception , e:
            print(e)
            pass

    def file_attributes(self,attr):
        self._attr=attr

    def rows(self,rows):
        self._rows=rows

    def create_yaml(self,rows,count):
        #count = count + 1
        filename=self.pathname () + self.filename(count) 
        print "writing %s" % filename
        self.outfile=open(filename,"w")        
        self.outfile.write( yaml.dump(
            { 
                'type': "chunk",
                'sourceurl' :   self.sourcefile,
                'filename'  :   self.name,
                'header'    :   self._attr,
                'countrows' :   len(rows),
                'rows'      :   rows,            
            }, 
            default_flow_style=False,
            Dumper=yaml.CDumper
        ))
        self.outfile.flush()
        self.outfile.close()
        print "going to checkin"
        checkin(self.pathname(), self.filename(count) )
        print "after checkin"
                   

        
    

class Fechout ():
    u"""
    Wrapper for fech, manage the zip file
    """
    def __init__(self):
        self.url=None

    def set_input_url(self, url):
        self.url=url

    def set_input_zipfilename(self, filename):
        self.zipfile=filename
        
    def create_file(self, name, sourcefile,baseurl, urlfile):
        return FechoutFile(name,sourcefile,baseurl, urlfile)



