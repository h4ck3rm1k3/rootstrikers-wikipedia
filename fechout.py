#encapsulate the output of fec
from yaml import load, dump
import os

def checkin(path):
    os.system("bash ./checkin.sh %s" % path)


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
        return "fech_yaml/%s/" % (self.sourcefile)

    def filename(self):
        self._filename = self.pathname() +  "/"  + self.name +  ".yml"
        return self._filename

    def exists(self):
        return os.path.exists(self.filename())

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

    def create_yaml(self):

#        print ('countrows' , len(self._rows),  'countraw' ,  len(self._raw))       
#        if (len(self._rows) ==len(self._raw))

        return dump(
            { 
                'sourceurl' :   self.sourcefile,
                'filename'  :   self.name,
                'header'    :   self._attr,
                'countrows' :   len(self._rows),
                'countraw'  :   len(self._raw),
                'rows'      :   self._rows,
#                'raw'       :   self._raw,
            }, 
            default_flow_style=False
    )


    def close(self):
        if (len(self._rows)>0):
            self.outfile=open(self.filename(),"w")
            self.outfile.write(self.create_yaml())
            self.outfile.flush()
            self.outfile.close()
            self.outfile=None
            
            checkin(self.filename())
        else:
            self.outfile=open(self.filename(),"w")
            self.outfile.write("\n".join(self._raw))
            raise Exception("no rows for %s %s" %( self.sourcefile, self.name))
    

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



