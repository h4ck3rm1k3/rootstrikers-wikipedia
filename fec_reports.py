
####
import getopt, sys
import lxml.html
import cache

def process(fecid, verbose) :
    #
    url="http://images.nictusa.com/cgi-bin/fecimg/?" + fecid
    data= cache.cacheweb(url)
    d = lxml.html.document_fromstring( data   )
    d.make_links_absolute(url)
    for (f_name_element, attr , f_link, pos) in d.iterlinks():
            if(attr == 'href'):
                print f_link
                data= cache.cacheweb(f_link)

def usage():
    print "--help"
    print "-f,--fecid read this fecid"
    print "-v --verbose"

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:v", ["help", "fecid=","verbose"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    fecid = None
    verbose = False
    print opts
    for o, a in opts:
        if o in ("-v" , "--verbose"):
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--fecid"):
            fecid = a
        else:
            assert False, "unhandled option"
    if fecid is not None :
        process(fecid,verbose)
    else:
        print "fec is none"
        usage()

if __name__ == "__main__":
    main()



