#!/usr/bin/python
import os
import CRP_IDs as crp
import legislators_current as leg
import dump
import cache 

from cStringIO import StringIO
crp= cache.cache('crp',crp.parse)
legs= leg.load()

def compare(a,b) :
    for x in sorted(a['wp'].keys()):
        aobj = a['wp'][x]
        if 'fec' not in aobj['id']:
            print "No fec for", aobj['name']
        else:
            for fec in aobj['id']['fec'] :
#                print fec
                if fec in b :
                    bobj = b[fec]
                    if 'opensecrets' in aobj['id'] :
                        if aobj['id']['opensecrets'] != bobj['CID'] :
                            #print bobj,aobj
                            print "fix secrets",aobj['name']['official_full'],aobj['id']['opensecrets'],bobj
                    else:
                        print "missing open secrets",aobj['name']['official_full'],bobj
                else:
#                    print "missing ",fec,"in b",aobj['name']['official_full']
                    pass
            
compare(legs,crp)
leg.apply(legs)
dump.dump(legs)
