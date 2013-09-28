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


import zipfile
import os
import cache
import fechout


import sys
#import fec.version.v1.F1
#import fec.version.v1 as v1

#print sys.path
#sys.path

# before we import these, we must define the base classes, do that here so we have everything in one file




BASEURL = 'ftp://ftp.fec.gov/FEC/electronic/'
def listing():
    u"""
    execute the listing
    """
    dirlisting = cache.cacheweb('ftp://ftp.fec.gov/FEC/electronic/')
    for filename in dirlisting.split():
        #print("consider file %s" % filename)
        if (filename.find(".zip") >0 ):
            #print("going to get file %s" % BASEURL + filename)
            cached_file = cache.cachewebfile(BASEURL + filename)
            #print("cached file %s" % cached_file)
            csv_data = ZipCSV()
#            parser = fech_rendered_maps.FieldParser()
            parser = Parser()
            output_object = fechout.Fechout()
            output_object.set_input_url(BASEURL + filename)
            output_object.set_input_zipfilename(filename)
            #parser.set_zipfilename(filename)

            csv_data.process_generate (
                BASEURL, 
                filename,
                cached_file,
                "FecElectronicFilings",
                parser,
                output_object)

class HDR:
# SEQ	 DESCRIPTION	TYPE	REQUIRED	DATA	REFERENCE	REFERENCE					
# 1	Record Type	A/N-3	X (error)	HDR	HDR	
# 2	EF Type	A/N-3	X (error)	FEC	FEC	
# 3	FEC Ver	A/N-4	X (error)	3.00		
# 4	Soft Name	A/N-90		SUPERIFLER		
# 5	Soft Ver	A/N-16		1.02		
# 6	Name Delim	A-1				Only if other than "^"
# 7	Rpt ID	A/N-16		FEC-1234		FEC report ID of original report (Amenment only)
# 8	Rpt Number	N-3		1	1,2,3,4	Sequential number of amenments
# 9	HDRcomment 	A/N-200				For testing only.
    def __init__(self,fields):
        self.field_count= len(fields)

        self.record_type=fields[0];
        self.EF_type=fields[1]; # FEC
        self.FEC_ver=fields[2]; #

        if (self.field_count> 3):
            self.soft_name=fields[3];
        else :
            print "check version3: %d %s " % (self.field_count,fields)

        if (self.field_count> 4):
            self.soft_ver=fields[4];
        else :

            print "check version4: %d %s " % (self.field_count,fields)

        if (self.field_count> 5):
            #print "before field 5: %d %s " % (self.field_count,fields)
            self.name_delim=fields[5];
        else:
            #                    0      1       2       3              4
            #check version6: 5 ['HDR', 'FEC', '3.00', 'Super Filer', 'Ver 1.0'] 

            #print "check version5: %d %s " % (self.field_count,fields)
            pass

        if (self.field_count> 6):
            self.report_id=fields[6];
        else:
            #print "check version6: %d %s " % (self.field_count,fields)
            pass

        if (self.field_count> 7):
            self.report_num=fields[7];
        else:
            #print "check version7: %d %s " % (self.field_count,fields)
            pass




class ZipCSV:

    def process_generate (self, baseurl, urlfile, filename, classname, parser, out):

        zfile = zipfile.ZipFile(filename)
        for name in zfile.namelist():
            (dirname, ifilename) = os.path.split(name)
            print "reading  filename %s from zip %s" %  (ifilename, filename)
            d = zfile.read(name)
            out_file = out.create_file(ifilename, filename, baseurl, urlfile)
            parser.parse_file_data(ifilename, filename, d, out_file)
            out_file.close()

def dbg (x):
#    traceback.print_stack(limit=2)
#    print (x)
    pass

class Document:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename
   
# global instance         
   
class Header:
    def __init__(self,header,fec,version):

        from  versions import Versions
        self.version_proc = Versions()

        self.header = header
        self.fec = fec
        self.version = version

    def version_factory(self):
        item= self.version_proc.lookup(self.version)
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
        self.state=STATE_UNKNOWN
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

        if line == 'Schedule_Counts:':
            return 

        parts = line.split('=')
        
        if (len(parts) > 1):
            self.current.attributes[parts[0]] = parts[1].strip().rstrip()
        else:
            raise Exception(line)

    def endHeader(self):
#        dbg ( "END HEADER" )
        self.state = STATE_BODY

    def HDR(self, l, quote=""):

        if l.find('HDRFEC') > -1 :
            self.sep=''
        else:
            self.sep=','

        parts = []
        count = 0
        for x in l.split(self.sep):
            x = x.replace("\"","")
            count = count +1
            parts.append(x)
        
        if count < 3 :
            self.state = STATE_BODY
            return None

        header = parts[0]
        fec = parts[1]
        version = parts[2]

        #dbg ( "HEADER LINE header %s fec %s version %s " % ( header, fec, version))
        #        self.version = Version(version)
        self.header=Header(header,fec,version)
        self.header_version = self.header.version_factory()
        self.header_version.set_sep(self.sep)
        self.header_version.parse(parts)
        self.state = STATE_BODY

    def delimiter(self, filing_version):
        if (filing_version.to_f < 6):
            return  ","
        return "\034"

    def filing_url(self):
        return "http://query.nictusa.com/dcdev/posted/#{filing_id}.fec"

    def parse_line(self, l):
        dbg ( "check '%s' '%d'" % (l, self.state))

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
            dbg ( "in header %s" %  l)
            self.header_line(l)
            return self.state

        if self.state == STATE_BODY:
            dbg ( "in body %s" % l)
            result = self.body_line(l)
            if result is None :
                self.state = STATE_END
                raise Exception("Body parse failed %s" % l) 
            return result

        if self.state == STATE_END:
            return None 
            # call into the base class fech_rendered_maps

        return None

    def find_version_info(self,line):
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
                    import fec.version.v1.F1
                    import fec.version.v1
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
            if self.header_version is not None:
                self.header_version.set_attr_hash(self.current.attributes)
            else:
                print("check version in : (%s)" % line )
                raise Exception("missing version")


    def body_line(self, line):
        u"""
        the body function
        """
        if self.header_version is None:
            self.find_version_info(line)

        if self.header_version is not None:
            result = self.header_version.parse_body(line) 
            if result is None :
                raise Exception("failed to parse body %s" % line)
            return result
        else:
            raise Exception("no version")
       

    # entry point into input, called from zipcsv.py
    def parse_file_data(self, filename, sourcefile, d, out_file):
        self.current = FileObject()

        try :
            for l in d.split("\n"):                
#                print ("Raw input:%s" % l)
                out_file.raw_line(l)
                result = self.parse_line(l)
#                print (result)

            #out_file.dir_name(dirname)
            out_file.file_attributes(self.current.attributes)
            if self.header_version is not None:
                try:
                    out_file.rows(self.header_version.record_list)
                except Exception, e:
                    traceback.print_exc()
                    print (e)
                    print (self.header_version)
            else:
                raise Exception("no header")

        except Exception, e:
            print "Parsing Failed filename %s source %s" % (filename, sourcefile)
            traceback.print_exc()
            raise e

        self.current = None

    def generate(self, v, name):
        c = 0

        for f in v:
            f = f.strip(" ").rstrip(" ")
            f = f.strip("\"").rstrip("\"")
            dbg ( "    %s=%d" % (f, c))
            c = c + 1

#main
listing()
