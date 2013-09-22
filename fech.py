# porting of fetch to python code borrowed from https://github.com/NYTimes/Fech
# wich is under the apache license
# https://github.com/NYTimes/Fech/blob/master/LICENSE
import re
import traceback 
#state enum
STATE_UNKNOWN = 0
STATE_HEADER = 1
STATE_BODY = 2

import sys
sys.path.append('./FEC-Field-Documentation')

import versions

def dbg (x):
#    traceback.print_stack(limit=2)
    print (x)

class Document:
    def __init__(self,url,filename):
        self.url=url
        self.filename=filename

class VersionsProc (Versions):
    def lookup(version):
        version  = version.replace(".","_")
        factory =self.versions[version]
        return factory()
   
# global instance         
version_proc = VersionsProc()
   
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

    def version_field_name (self):
        return  u"FEC_Ver_\#"

    def __init__(self):
        self.header=None

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
            self.current.attributes[parts[0]] = parts[1]


    def endHeader(self):
#        dbg ( "END HEADER" )
        self.state = STATE_BODY

    def HDR(self, l, quote=""):

        parts = l.split(",")
        header = parts[0]
        fec = parts[1]
        version = parts[2]
        dbg ( "HEADER LINE header %s fec %s version %s " % ( header, fec, version))
        #        self.version = Version(version)
        self.header=Header(header,fec,version)
        version = self.header.version_factory()
        version.parse(parts)
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
            dbg ( "in body %s" % l)
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
                #         print ("check version: ",
                #                "version:",version,
                #                "attr:",self.current.attributes
                #            )
        else:
            print("no version: ",
                  "version:", version,
                  "attr:", self.current.attributes
                  )

        body = line.split(",")
        for field_regex in self.rendered_maps.keys():
            btype = body[0]

            g = re.findall("(" + field_regex + ")", btype, re.IGNORECASE)
            if (g is not None):
                if (len(g) > 0):
                    print("check: ",
                          "regex:", field_regex,
                          "group", g,
                          "btype:", btype,
                          "version:", version,
                          "body:", body)

                    if (version is not None):
                        for version_regex in self.rendered_maps[field_regex].keys():
                            rest_of_data = self.rendered_maps[
                                field_regex][version_regex]
                            #TODO: use rest_of_data
                            g = re.findall(
                                "(" + version_regex + ")",
                                version,
                                re.IGNORECASE)
                            if (g is not None):
                                if (len(g) > 0):
                                    print(
                                        "check2: ", field_regex, g, btype, version, body, self.rendered_maps[field_regex][version_regex])

        #print l
        #                v=l.split("")
        #                self.generate(v,classname)
        #                return

    def parse_file_data(self, d):
        self.current = FileObject()
        for l in d.split("\n")[0:20]:
            self.parse_file_data_line(l)

            if (self.state == STATE_BODY):
                return 

        dbg ( "COLLECTED %s" % self.current.attributes)
        self.current = None

    def generate(self, v, name):
        c = 0

        for f in v:
            f = f.strip(" ").rstrip(" ")
            f = f.strip("\"").rstrip("\"")
            dbg ( "    %s=%d" % (f, c))
            c = c + 1
