import os
#import socrata_rows as soc
import Current_members_of_the_United_States_House_of_Representatives as reps
import List_of_current_United_States_Senators as sens
import cache 
import legislators_current as leg

from cStringIO import StringIO

rep= cache.cache('reps',reps.parse_rep)
#rep= reps.parse_rep()
sen= cache.cache('sen',sens.parse)

congress = { 'wp' : rep['wp'].copy() }
congress['wp'].update(sen['wp'])
legs= leg.load()

#print "REPS:",sorted(rep['wp'].keys())
#print "SEN:",sorted(sen['wp'].keys())
#print "TOTAL:",sorted(congress['wp'].keys())
#print "Legs:",sorted(legs['wp'].keys())

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
            print 'in b no ' + name ,  "IN A: ", name + ": " + str(aobj['links'][name]), bobj['id']
#        else:
#            print 'in b no ' + name ,   "not in a",bobj['id'],

def compare(a,b) :

    for x in sorted(a['wp'].keys()):
        aobj = a['wp'][x]
        if x in b['wp'] :
            bobj = b['wp'][x]

            if 'links' in aobj :
                check(aobj,bobj,'bioguide')               
                check(aobj,bobj,'votesmart')
            else:
                print 'no links' 
                print aobj                
        else:
            print "Missing %s " % x
 #           print aobj


print "Wikipedia\n"
#print congress
compare(congress,legs)
#print "Legs\n"
#compare(legs,congress)
# for x in sorted(legs['wp'].keys()):
#     if 'bioguide' not in legs['wp'][x]['id']:
#         print  " missing bioguide " + x 

#     if 'votesmart' not in legs['wp'][x]['id']:
#         print  " missing votesmart " + x 
