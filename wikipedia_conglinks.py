import wiki
import legislators_current
import dump

import getopt, sys

def usage():
    print "--help"

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
    for x in sorted(legs['wp'].keys()):
        print x        
        wiki.parse_wiki_source(x,legs)
    dump.dump(legs)

if __name__ == "__main__":
    main()
