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
          

def compare(a,b,name,link) :
    for x in sorted(a['wp'].keys()):
        aobj = a['wp'][x]
#        print aobj['id']
        if link not in  aobj['id']:
            pass
        else:
            bid = aobj['id'][link]
            bid = bid.replace(" ","_")
            if bid not in b['wp'] :
 #               print "missing in B ", bid
#                print sorted(b['wp'].keys())
                continue
                
            bobj = b['wp'][bid]

            if name in  bobj['links']:
                val = bobj['links'][name]
                a['wp'][x]['id'][name]=val
                print "transfered",name,link,val


compare(legs,rep,'opencong','wikipedia')
compare(legs,sen,'opencong','wikipedia')

compare(legs,brep,'opencong','ballotpedia')
compare(legs,bsen,'opencong','ballotpedia')


import dump
leg.apply(legs)
dump.dump(legs)
