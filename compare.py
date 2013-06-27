#!/usr/bin/python
import os
#import socrata_rows as soc
import Current_members_of_the_United_States_House_of_Representatives as reps
import Ballotpedia_house as breps
import List_of_current_United_States_Senators as sens
import Ballotpedia_senator as bsens
import cache 
import legislators_current as leg

from cStringIO import StringIO

rep= cache.cache('reps',reps.parse_rep)
brep= cache.cache('breps',breps.parse)
sen= cache.cache('sen',sens.parse)
bsen= cache.cache('bsen',bsens.parse)

congress = { 'wp' : rep['wp'].copy() }
congress['wp'].update(sen['wp'])
legs= leg.load()

def check(aobj,bobj,name):
    if name in bobj['id'] :
        bval= str(bobj['id'][name])
        if name in aobj['links'] :
            aval = str(aobj['links'][name])
            if aval != bval :
#                print "aval " ,aval
                print "Found " , name,  aval, "/", bval
#        else:
#            print 'in a no :' + name , aobj['links']
    else:
        if name in aobj['links'] :
            val = str(aobj['links'][name])
            print 'in b no ' + name ,  "IN A: ", name + ": " + val, bobj['id']
            bobj['id'][name]=val
        else:
            print 'in b no ' + name ,   "not in a",bobj['id']

def compare(a,b) :
    for x in sorted(a['wp'].keys()):
        aobj = a['wp'][x]
        if x in b['wp'] :
            bobj = b['wp'][x]
            if 'links' in aobj :
                check(aobj,bobj,'bioguide')               
                check(aobj,bobj,'votesmart')
                check(aobj,bobj,'ballot')
            else:
                print 'no links' 
                print aobj                

        if 'wikipedia' not in  aobj['links']:
            print "Missing wikipedia in BP %s " % x, aobj
        else:
            print "Missing %s " % x
            

def compare_bpr(a,b) :
    for x in sorted(a['wp'].keys()):
        aobj = a['wp'][x]
#        print aobj
        if 'wikipedia' not in  aobj['links']:
            print "Missing wikipedia in BP %s " % x, aobj
        else:
            wp = aobj['links']['wikipedia']
            if wp in b['wp'] :
                bobj = b['wp'][wp]
                if 'links' in aobj :
                    if 'ballot' in  bobj['links']:
                        ballot = bobj['links']['ballot']
                    else:
                        #print 'no BP in wikipedia article '  , wp, bobj
                        # now we save the new ballotpedia link that we inferred
                        b['wp'][wp]['links']['ballot']=x
                else:
                    print 'no links' 
                    print aobj                
            else:
                print "Missing %s in wikipedia, wrong link" % x, aobj

compare_bpr(brep,rep)
compare_bpr(bsen,sen)
compare(congress,legs)

import dump
leg.apply(legs)
dump.dump(legs)
