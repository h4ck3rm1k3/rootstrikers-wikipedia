# porting of fetch to python code borrowed from https://github.com/NYTimes/Fech
# wich is under the apache license
# https://github.com/NYTimes/Fech/blob/master/LICENSE


class RecordsBase:
    def __init__(self):
        pass
    def hash_names(self, fields):
        names={}
        for f in fields:
            names[f['name']]=f
        return names

    def parse(self,fields,line):

        expected_count=len(self.fields)
        input_count   =len(fields)
        result={}
        result["input"]=line
        result["result"]=[]

        #copy of fields
        fields2=fields

        if not input_count == expected_count :
            #print ("%s != %s" % (expected_count,    input_count))
            result["expected_count"]=expected_count
            result["input_count"]=input_count


            result["attempt"]=[]

            # now just fill out what we can
            for field_descriptor in self.fields:
                if (len(fields2)>0):
                    v = fields2.pop(0)
                    field_descriptor["value"]=v
                else:
                    field_descriptor["value"]="NO VALUE!"

                result["attempt"].append(field_descriptor)

            # now the rest of the fields
            while len(fields2)>0:
                v = fields2.pop(0)
                field_descriptor ={"value": v}
                result["attempt"].append(field_descriptor)

            return result


        # exact match
        # now just fill out what we can
        for field_descriptor in self.fields:
            v = fields2.pop(0)
            field_descriptor["value"]=v
            result["result"].append(field_descriptor)
        return result

class VersionBase:

      def __init__(self):
            self.do_init()


      def set_sep(self, sep):
            self.sep=sep

      def do_init(self):
            self.record_list=[]
            self.sep=","

      def parse(self,x):
            fieldtype=x[0]
            if fieldtype == "HDR":
                  self.hdr=HDR(x)
                  self.hdr.emit()
            else:
                  #print "Version Base, parse," + str(x)
                  pass
            
            #raise Exception(x)

      def parse_record(self,fields, record_type,line):
            self.current_record=self.records[record_type]()
            result = self.current_record.parse(fields,line)
            self.record_list.append(result)            
            return result

      def parse_body(self,line):
            fields_temp=line.split(self.sep)
            fields=[]
            for f in fields_temp:
                  f=f.replace('\"',"")
                  fields.append(f)
            record_type=fields[0]
            original_record_type=record_type

            if record_type == "": 
                  raise Exception("record type none")
                  #return None 

            if record_type == "[BEGINTEXT]": 
                  raise Exception("skip mail file")
                  #return None 

            if record_type == "[BEGIN TEXT]": 
                  raise Exception("skip mail file")
                  #return None 

            #hack
            if record_type == "H4":
                  record_type = "SH4"

            if record_type == "H1":
                  record_type = "SH1"

            if record_type == "H2":
                  record_type = "SH2"

            if record_type == "H3":
                  record_type = "SH3"

            if record_type in self.records:                  
                  return self.parse_record(fields,record_type,line)
            else:
                  record_type=record_type[:2]
                  if record_type in self.records:                  
                        return self.parse_record(fields,record_type,line)
                  else:
                        raise Exception("recordtype '%s' original_record_type %s not known %s record %s" % (record_type, original_record_type, sorted(self.records.keys()), str(fields) ))
                        #'F3' : fec.version.v1.F3.Records,
            raise Exception()
            #return  

      def set_attr_hash(self, attrdict):
            self.record_list=[]
            

class VersionsBase:
    def __init__(self):
        pass 
    def lookup(self,version):
        orginal_version=version

        if version == "5.00":
            return self.versions["v5.0"]()
        elif version == "5.10":
            return self.versions["v5.1"]()
        elif version == "5.20":
            return self.versions["v5.2"]()
        elif version == "5.30":
            return self.versions["v5.3"]()
        elif version == "v3.0":
            return self.versions["v3"]()
        elif version == "3.0":
            return self.versions["v3"]()
        else:
            version  = version.replace(".00","")
            version = "v" + version
            version  = version.replace("\"","")
            if version in  self.versions:
                factory =self.versions[version]
                return factory()
            else:
                raise Exception("version '%s'/'%s' not in %s " % (orginal_version,version,sorted(self.versions.keys)))
        
