import legislators_current as leg
import datetime

def dord(day):
    day=int(day)
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]

    return "%d%s" % (day, suffix)


def process(filename,verbose):
    if verbose :
        print ("reading", filename)
    ################################################
    f = open(filename,"rb")

    wiki = open(filename + '.wiki', "wb")
    table = open(filename + '.wikitable', "wb")

    legs=leg.load()

    ## index
    fecids={}
    for x in sorted(legs['wp'].keys()):
        if 'fec' in legs['wp'][x]['id']:
            for field in legs['wp'][x]['id']['fec']:
                fecids[field]=legs['wp'][x]
            #else:
            #print "no fec", legs['wp'][x]

    ################################################
    d = f.read()
    for l in d.split("\n"):
        if l[0:4] == "SB23" :
#            print "---"
            fields=l.split("")
            i=0
            for f in fields:
                i = i +1
            f=fields
            date = f[19]
            amount = float(f[20])
            if amount < 0 :
                continue
            fromfec = f[1]
            fec = f[24]
            fec2 = f[26]
            campaign = f[22]
            committee =f[6]
            name = ' '.join([ f[28],f[29], f[27]])
            state = f[33]

            if (fec2 in fecids):
                date = datetime.datetime.strptime(date, "%Y%m%d")
                day = dord(date.strftime("%d"))
                m = date.strftime("%B")
                y = date.strftime("%Y")
                date = "%s %s %s" % (m,day,y)
                tablestr= "|-\n|[[%s]]\n| [[%s]]\n| $%s\n| %s | %s | '''%s'''" %  ( fromfec, fecids[fec2]['id']["wikipedia"] , amount, date, campaign,committee  )
                table.write(tablestr )
                wikistr=" * [[%s]] %s donated $%s on %s to the %s via '''%s'''." %  (fecids[fec2]['id']["wikipedia"], fromfec, amount, date, campaign,committee  )
                wiki.write( wikistr)
#                print wikistr

            else:
                print "fec2 missing", fec2, fields

    wiki.close()
    table.close()


####
import getopt, sys

def usage():
    print "--help"
    print "-f,--file read this file"
    print "-v --verbose"

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:v", ["help", "file=","verbose"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    filename = None
    verbose = False
    print opts
    for o, a in opts:
        if o in ("-v" , "--verbose"):
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--file"):
            filename = a
        else:
            assert False, "unhandled option"
    if filename is not None :
        process(filename,verbose)
    else:
        print "Filename is none"

if __name__ == "__main__":
    main()

