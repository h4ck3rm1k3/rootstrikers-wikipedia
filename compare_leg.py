#!/usr/bin/python
import os
import legislators_current as leg
import legislators_other as leg2
import re
import dump
import cache 

from cStringIO import StringIO
legs= leg.load()
legs2= leg2.load()

def compare(a,b,field,convertInt) :
    for x in sorted(a['wp'].keys()):
        aobj = a['wp'][x]
        bobj = b['wp'][x]
        if field  in aobj['id'] :
            ml = aobj['id'][field]
            if convertInt :
                match= re.search('(\d+)', str(ml))
                if (match):
                    ml = match.group(1)
            b['wp'][x]['id'][field]=ml
            print "updated", field ,"for id" ,x, ml
        else :
            print "missing", field ,"in source" ,x


import getopt, sys

def usage():
    print "--help"
    print "-i,--int convert value to int"
    print "-f fieldname,--field=fieldname"

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hif:v", ["help", "field=", "int"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    field = None
    verbose = False
    convertInt=False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--field"):
            field = a
        elif o in ("-i", "--int"):
            convertInt=True
        else:
            assert False, "unhandled option"

    compare(legs,legs2,field,convertInt)
#    leg.apply(legs)
    dump.dump(legs2)


if __name__ == "__main__":
    main()
