import wiki
import legislators_current
import dump

import getopt, sys

def usage():
    print "--help"

def check_imdb(x,A,B) :
    a=None
    b=None
    if "imdb" in  A['id']:
        a =A['id']['imdb']
    if 'imdb' in B:
        b=B['imdb']
    if b is not None:
        if b.find("nm") > 0 :
            print x,a,b

def check_wikipedia(x,A,B) :
    a=None
    b=None
    k="wikipedia"
    if k in  A['id']:
        a =A['id'][k]
    if k in B:
        b=B[k]
    if b is not None:
        print x,a,b

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv", [])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    verbose = False

    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option"

    legs= legislators_current.load()
    #print legs
    #    print legs['wp'].keys()
    #    print legs['wp'].items()
    names = sorted(legs['wp'].keys())
#    print names
    for x in  names:
#        print legs['wp'][x]
        try :
            d =wiki.parse_wiki_source(x,legs)
            A = legs['wp'][x]
            check_imdb(x,A,d)
            check_wikipedia(x,A,d)

        except Exception,e:
            print "error1:",e
    dump.dump(legs)

if __name__ == "__main__":
    main()
