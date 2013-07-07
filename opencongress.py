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

def load():
    legs= leg.load()
    for x in sorted(legs['wp'].keys()):
        idsobj= legs['wp'][x]['id'] 
    
        if 'govtrack' in idsobj:
            congid = idsobj['govtrack']
            cache.cacheweb('http://api.opencongress.org/people?person_id=%d' % congid)



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
