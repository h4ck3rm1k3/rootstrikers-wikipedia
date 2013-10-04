#encapsulate the output of fec
import yaml
#from 
import os

def checkin(path):
    print "going to process %s" % path
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

    def filename(self, count =0):

        self._filename = self.pathname() +  self.name 

        if (count > 0):
            # chunk
            self._filename = self._filename +  "_%d" % count
                    
        self._filename = self._filename +  ".yml"

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


    def chunks(self):
        """ Yield successive n-sized chunks from l.
        http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
        """
        n=2000
        for i in xrange(0, len(self._rows), n):
            yield self._rows[i:i+n]

    def create_yaml(self):

        total = len(self._rows)
        if (total > 2000):
            count = 0
            for chunk in self.chunks():
                count = count + 1
                filename=self.filename(count) 
                print "writing %s" % filename
                self.outfile=open(filename,"w")        
                self.outfile.write( yaml.dump(
                    { 
                        'type': "chunk",
                        'sourceurl' :   self.sourcefile,
                        'filename'  :   self.name,
                        'header'    :   self._attr,
                        'countrows' :   len(self._rows),
                        'countraw'  :   len(self._raw),
                        'rows'      :   chunk,            
                    }, 
                    default_flow_style=False,
                    Dumper=yaml.CDumper
                ))
                self.outfile.flush()
                self.outfile.close()
                print "going to checkin"
                checkin(filename)
                print "after checkin"

            #####
            #write the header
            self.outfile=open(self.filename(),"w")        
            self.outfile.write( yaml.dump(
                { 
                    'type': "header",
                    'sourceurl' :   self.sourcefile,
                    'filename'  :   self.name,
                    'header'    :   self._attr,
                    'countrows' :   len(self._rows),
                    'countraw'  :   len(self._raw),
                    "chunks"    :   count
                }, 
                default_flow_style=False,
                Dumper=yaml.CDumper                
            ))
            self.outfile.flush()
            self.outfile.close()
            self.outfile=None
            print "going to checkin"
            checkin(self.filename())
            print "after checkin"
        else:
            count =  1
            filename=self.filename() 
            print "writing %s" % filename
            self.outfile=open(filename,"w")        
            self.outfile.write( yaml.dump(
                { 
                    'type': "single",
                    'sourceurl' :   self.sourcefile,
                    'filename'  :   self.name,
                    'header'    :   self._attr,
                    'countrows' :   len(self._rows),
                    'countraw'  :   len(self._raw),
                    'rows'      :   self._rows,            
                }, 
                default_flow_style=False,
                Dumper=yaml.CDumper
            ))
            self.outfile.flush()
            self.outfile.close()
            print "going to checkin"
            checkin(filename)
            print "after checkin"
            

    def close(self):
        if (len(self._rows)>0):
            self.create_yaml()
                       
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



