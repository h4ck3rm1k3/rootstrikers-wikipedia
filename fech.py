# porting of fetch to python code borrowed from https://github.com/NYTimes/Fech
# wich is under the apache license
# https://github.com/NYTimes/Fech/blob/master/LICENSE
import re
import traceback 
#state enum
STATE_UNKNOWN = 0
STATE_HEADER = 1
STATE_BODY = 2
STATE_END = 3

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
    #print (x)
    pass

class Document:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

   
# global instance         
version_proc = versions.Versions()
   
class Header:
    def __init__(self,header,fec,version):
        self.header = header
        self.fec = fec
        self.version = version

    def version_factory(self):
        item= version_proc.lookup(self.version)
        item.do_init()
        return item

class FileObject:
    def  __init__(self):
        self.attributes = {}


class Parser:

    def set_zipfilename(self, zipfile):
        self.zip_filename = zipfile

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

        parts = []
        for x in l.split(","):
            x = x.replace("\"","")
            parts.append(x)
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
            return self.state

        if re.match(r'\/\* End Header', l):
            self.endHeader()
            return self.state

        if re.match(r'HDR', l):
            self.HDR(l)
            return self.state

        if re.match(r'\'HDR\'', l):
            self.HDR(l, quote='\'')
            return self.state

        if re.match(r'\"HDR\"', l):
            self.HDR(l, quote='\"')
            return self.state

        if self.state == STATE_HEADER:
#            dbg ( "in header %s" %  l)
            self.header_line(l)
            return self.state

        if self.state == STATE_BODY:
            #dbg ( "in body %s" % l)
            result = self.body_line(l)
            if result is None :
                self.state = STATE_END
                return None

        if self.state == STATE_END:
            return None 
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
                if re.match(r'1\..+', version  ):
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
            result = self.header_version.parse_body(line) 
            if result is None :
                return result
       

            # entry point into inptu
    def parse_file_data(self, filename, dirname, d, out_file):
        self.current = FileObject()
        try :
            for l in d.split("\n")[0:20]:
                result = self.parse_file_data_line(l)
                if result is None :
                    return 
        except:
            print "Parsing Failed"
            traceback.print_exc()

        out_file.dir_name(dirname)
        out_file.file_attributes(self.current.attributes)
        if self.header_version is not None:

            try:
                out_file.rows(self.header_version.record_list)
            except Exception, e:
                traceback.print_exc()
                print (e)
                print (self.header_version)


        self.current = None

    def generate(self, v, name):
        c = 0

        for f in v:
            f = f.strip(" ").rstrip(" ")
            f = f.strip("\"").rstrip("\"")
            dbg ( "    %s=%d" % (f, c))
            c = c + 1
