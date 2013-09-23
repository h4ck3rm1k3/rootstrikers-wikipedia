# porting of fetch to python code borrowed from https://github.com/NYTimes/Fech
# wich is under the apache license
# https://github.com/NYTimes/Fech/blob/master/LICENSE
import re
import traceback 
#state enum
STATE_UNKNOWN = 0
STATE_HEADER = 1
STATE_BODY = 2

import fec.version.v1
import fec.version.v2
import fec.version.v3
import fec.version.v5_0
import fec.version.v5_1
import fec.version.v5_2
import fec.version.v5_3
import fec.version.v6_1
import fec.version.v6_2
import fec.version.v6_3
import fec.version.v6_4
import fec.version.v7_0
import fec.version.v8_0


import versions

def dbg (x):
#    traceback.print_stack(limit=2)
    print (x)

class Document:
    def __init__(self,url,filename):
        self.url=url
        self.filename=filename

   
# global instance         
version_proc = versions.Versions()
   
class Header:
    def __init__(self,header,fec,version):
        self.header=header
        self.fec=fec
        self.version=version

    def version_factory(self):
        return version_proc.lookup(self.version)

class FileObject:
    def  __init__(self):
        self.attributes = {}


class Parser:

    def set_zipfilename(self,zipfile):
        self.zip_filename=zipfile

    def version_field_name (self):
        return  u"FEC_Ver_# "

    def __init__(self):
        self.zip_filename=None
        self.header=None
        self.header_version=None
        # Converts symbols and strings to Regexp objects for use in regex-keyed maps.
        # Assumes that symbols should be matched literally, strings unanchored.
        # @param [String,Symbol,Regexp] label the object to convert to a Regexp
    def regexify(self, label):
        if label in self.row_types_regex:
            return self.row_types[label]
        else:
            return r"^#{label.to_s}$"

    def startHeader(self):
        self.state = STATE_HEADER
#        dbg ( "start HEADER")

    def header_line(self, line):
        parts = line.split('=')
        if (len(parts) > 1):
            self.current.attributes[parts[0]] = parts[1].strip().rstrip()


    def endHeader(self):
#        dbg ( "END HEADER" )
        self.state = STATE_BODY

    def HDR(self, l, quote=""):

        parts = l.split(",")
        header = parts[0]
        fec = parts[1]
        version = parts[2]
        #dbg ( "HEADER LINE header %s fec %s version %s " % ( header, fec, version))
        #        self.version = Version(version)
        self.header=Header(header,fec,version)
        self.header_version = self.header.version_factory()
        self.header_version.parse(parts)
        self.state = STATE_BODY

    def delimiter(self, filing_version):
        if (filing_version.to_f < 6):
            return  ","
        return "\034"

    def filing_url(self):
        return "http://query.nictusa.com/dcdev/posted/#{filing_id}.fec"

    def parse_file_data_line(self, l):
    #        if re.match(r'\034',l):
        if l.find("\034") > 0:
            dbg ( "found 034 in %s" % l)
            #if first.index("\034").nil?

        if re.match(r'\/\* Header', l):
            self.startHeader()
            return

        if re.match(r'\/\* End Header', l):
            self.endHeader()
            return
        if re.match(r'HDR', l):
            self.HDR(l)
            return
        if re.match(r'\'HDR\'', l):
            self.HDR(l, quote='\'')
            return
        if re.match(r'\"HDR\"', l):
            self.HDR(l, quote='\"')
            return

        if self.state == STATE_HEADER:
#            dbg ( "in header %s" %  l)
            self.header_line(l)
            return

        if self.state == STATE_BODY:
            #dbg ( "in body %s" % l)
            self.body_line(l)
            # call into the base class fech_rendered_maps


    def body_line(self, line):
        u"""
        the body function
        """
        version = None
        version_field_name = self.version_field_name()
        if version_field_name in self.current.attributes:
                version = self.current.attributes[version_field_name]
#                print ("check version: ",
#                       "version:",version,
#                       "attr:",self.current.attributes
#                )
                if self.header_version is None:
                    if re.match(r'1\..+',version  ):
                        self.header_version= fec.version.v1.Version()
                        self.header_version.set_attr_hash(self.current.attributes)                               
                    elif re.match(r'2\..+',version  ):
                        self.header_version= fec.version.v2.Version()
                        self.header_version.set_attr_hash(self.current.attributes)
                    elif re.match(r'3\..+',version  ):
                        self.header_version= fec.version.v3.Version()
                        self.header_version.set_attr_hash(self.current.attributes)
                    elif re.match(r'5\.0.+',version  ):
                        self.header_version= fec.version.v5_0.Version()
                        self.header_version.set_attr_hash(self.current.attributes)
                    elif re.match(r'5\.1.+',version  ):
                        self.header_version= fec.version.v5_1.Version()
                        self.header_version.set_attr_hash(self.current.attributes)
                    elif re.match(r'5\.2.+',version  ):
                        self.header_version= fec.version.v5_2.Version()
                        self.header_version.set_attr_hash(self.current.attributes)
                    elif re.match(r'5\.3.+',version  ):
                        self.header_version= fec.version.v5_3.Version()
                        self.header_version.set_attr_hash(self.current.attributes)
                    elif re.match(r'6\.1.+',version  ):
                        self.header_version= fec.version.v6_1.Version()
                        self.header_version.set_attr_hash(self.current.attributes)
                    elif re.match(r'6\.2.+',version  ):
                        self.header_version= fec.version.v6_2.Version()
                        self.header_version.set_attr_hash(self.current.attributes)
                    elif re.match(r'6\.3.+',version  ):
                        self.header_version= fec.version.v6_3.Version()
                        self.header_version.set_attr_hash(self.current.attributes)
                    elif re.match(r'6\.4.+',version  ):
                        self.header_version= fec.version.v6_4.Version()
                        self.header_version.set_attr_hash(self.current.attributes)
                    elif re.match(r'7\..+',version  ):
                        self.header_version= fec.version.v7.Version()
                        self.header_version.set_attr_hash(self.current.attributes)
                    elif re.match(r'8\..+',version  ):
                        self.header_version= fec.version.v8.Version()
                        self.header_version.set_attr_hash(self.current.attributes)
                    else:
                        raise Exception()

        else:
            #print("no version: (%s)" % version_field_name,
            #      "version:", version,
            #      "attr:", self.current.attributes
            #      )
            self.header_version.set_attr_hash(self.current.attributes)


        if self.header_version is not None:
            self.header_version.parse_body(line)
       

    def parse_file_data(self, filename, dirname, d):
        self.current = FileObject()
        try :
            for l in d.split("\n")[0:20]:
                self.parse_file_data_line(l)
        except:
            print "Parsing Failed"
            traceback.print_exc()

        dbg( "ZIPFILE %s" % self.zip_filename)
        dbg( "FILENAME %s" % filename)
        dbg( "DIRNAME %s" % dirname)
        #dbg ( "FINISHED_COLLECTED %s" % self.current.attributes)
        #dbg ( "FINISHED_DATA %s" % str(self.header_version.record_list))

        
        #self.record_list

        self.current = None

    def generate(self, v, name):
        c = 0

        for f in v:
            f = f.strip(" ").rstrip(" ")
            f = f.strip("\"").rstrip("\"")
            dbg ( "    %s=%d" % (f, c))
            c = c + 1
