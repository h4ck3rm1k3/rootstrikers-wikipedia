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

def compare(a,b,field,field2,convertInt,verbose) :
    for x in sorted(a['wp'].keys()):
        aobj = a['wp'][x]
        bobj = b['wp'][x]
        v2 = None
        if (not field2 is None) and (field2  in aobj['id'] ) :
            v2 = aobj['id'][field2]
        else:
            if (verbose) :
                print "missing", field2 ,"in " ,x
        if field  in aobj['id'] :
            v = aobj['id'][field]
            if convertInt :
                match= re.search('(\d+)', str(v))
                if (match):
                    v = match.group(1)                
            b['wp'][x]['id'][field]=v
            if (verbose) :
                print "updated", field ,"for id" ,x, v
        else :
            if (v2 is None ):
                print "missing", field ,"in source" ,x
            else:
                if (verbose) :
                    print "updated", field ,"for id" ,x, v2
                b['wp'][x]['id'][field]=v2

import getopt, sys

def usage():
    print "--help"
    print "-i,--int convert value to int"
    print "-f fieldname,--field=fieldname"
    print "-g fieldname,--field2=fieldname2"

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hifg:v", ["help", "field=","field2=", "int"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    field = None
    field2 = None
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

        elif o in ("-g", "--field2"):
            field2 = a

        elif o in ("-i", "--int"):
            convertInt=True
        else:
            assert False, "unhandled option"

    compare(legs,legs2,field,field2,convertInt,verbose)
#    leg.apply(legs)
    dump.dump(legs2)


if __name__ == "__main__":
    main()
