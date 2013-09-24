u"""
Produce a wikitable based on the fec data
the output files are written next to the input files
"""

import legislators_current as leg
import datetime
import getopt
import sys


def dord(day):
    u"""
    day ordinal, inflect the day
    """
    day = int(day)
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    return "%d%s" % (day, suffix)


def format_date(date):
    u"""
    format the date
    """
    date = datetime.datetime.strptime(date, "%Y%m%d")
    record_day = dord(date.strftime("%d"))
    record_month = date.strftime("%B")
    record_year = date.strftime("%Y")
    return  "%s %s %s" % (record_month, record_day, record_year)


def wikify_fields(fecids, fields, table, wiki):
    u"""
    Wikify the fields, and write them to the table as well
    """

    date = fields[19]
    amount = float(fields[20])
    fromfec = fields[1]
    #fec = fields[24]
    fec2 = fields[26]
    campaign = fields[22]
    committee = fields[6]
    #name = ' '.join([fields[28], fields[29], fields[27]])
    #state = fields[33]

    if (fec2 in fecids):
        tablestr = (
            "|-\n|[[%s]]\n|"
            " [[%s]]\n| $%s\n| %s | %s | '''%s'''" % (
                fromfec,
                fecids[fec2]['id']["wikipedia"],
                amount,
                format_date(date),
                campaign,
                committee
            )
        )
        table.write(tablestr.encode("UTF-8"))
        wikistr = (
            " * [[%s]] %s donated $%s on %s "
            "to the %s via '''%s'''." % (
                fecids[fec2]['id']["wikipedia"],
                fromfec,
                amount,
                date,
                campaign,
                committee
            )
        )
        wiki.write(wikistr.encode("UTF-8"))


def process(filename, verbose):
    u"""
    Process the file
    """
    if verbose:
        print("reading", filename)
    #
    fileobj = open(filename, "rb")
    wiki = open(filename + '.wiki', "wb")
    table = open(filename + '.wikitable', "wb")
    legs = leg.load()
    # index
    fecids = {}
    for fec_id in sorted(legs['wp'].keys()):
        if 'fec' in legs['wp'][fec_id]['id']:
            for field in legs['wp'][fec_id]['id']['fec']:
                fecids[field] = legs['wp'][fec_id]


    for line in fileobj.read().split("\n"):
        if line[0:4] == "SB23":
        #            print "---"
            fields = line.split("")
            wikify_fields(fecids, fields, table, wiki)
    wiki.close()
    table.close()


def usage():
    u"""
    print usage
    """
    print "--help"
    print "-f,--file read this file"
    print "-v --verbose"


def main():
    u"""
    main routine
    """
    try:
        (opts, args) = getopt.getopt(
            sys.argv[1:],
            "hf:v",
            ["help",
             "file=",
             "verbose"]
        )
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    filename = None
    verbose = False
    print (opts, args)
    for opt, value in opts:
        if opt in ("-v", "--verbose"):
            verbose = True
        elif opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-f", "--file"):
            filename = value
        else:
            assert False, "unhandled option"
    if filename is not None:
        process(filename, verbose)
    else:
        print "Filename is none"

if __name__ == "__main__":
    main()
