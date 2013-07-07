import re
import json
import encode
import dump
from pprint import pprint
import legislators_current as leg
import cache 
 
"""
extract open congress data and records
"""
import getopt, sys
from lxml import etree
from StringIO import StringIO
def load():
    legs= leg.load()
    for x in sorted(legs['wp'].keys()):
        idsobj= legs['wp'][x]['id'] 
        name = legs['wp'][x]['name']['official_full'] 
        congid = idsobj['govtrack']
        xml = cache.cacheweb('http://api.opencongress.org/people?person_id=%d' % congid)
#       print len(xml)
        xml =xml.replace("<?xml version=\"1.0\" encoding=\"UTF-8\"?>","")
        xmlio = StringIO(xml)

        tree = etree.parse(xmlio)
        name =  unicode(tree.xpath("//unaccented-name/text()")[0])
        name = name.replace(" ","_")
        url = "http://www.opencongress.org/w/index.php?title=%s&printable=yes" % name
        #url = "http://www.opencongress.org/wiki/%s" % name
        try :
            data = cache.cacheweb( url)
        except Exception, e:
            print "failed", name ,e
        except KeyboardInterrupt:
            print "bye"
            exit()
        
        #       print data 
#        if 'govtrack' in idsobj:
 #          congid = idsobj['govtrack']
           # xml = cache.cacheweb('http://api.opencongress.org/people?person_id=%d' % congid)
           #some_file_like_object = BytesIO("<root>data</root>")

        #print etree.tostring(tree)




def usage():
    print "--help --verbose"


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv", ["help", "verbose"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    verbose = False
    convertInt=False
    for o, a in opts:
        if (o == "-v", "--verbose"):
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option"

    load()



if __name__ == "__main__":
    main()
