import os
#import socrata_rows as soc
import Current_members_of_the_United_States_House_of_Representatives as reps
import List_of_current_United_States_Senators as sens
import cache 
import legislators_current as leg

from cStringIO import StringIO

rep= cache.cache('reps',reps.parse_rep)
sen= cache.cache('sen',sens.parse)

congress = { 'wp' : rep['wp'].copy() }
congress['wp'].update(sen['wp'])
legs= leg.load()

print "REPS:",sorted(rep['wp'].keys())
print "SEN:",sorted(sen['wp'].keys())
print "TOTAL:",sorted(congress['wp'].keys())
print "Legs:",sorted(legs['wp'].keys())

def compare(a,b) :
#    print a['wp']
    for x in sorted(a['wp'].keys()):
        aobj = a['wp'][x]
        if x in b['wp'] :
#            print "Found %s " % x
 #           print aobj
            pass
        else:
            print "Missing %s " % x
 #           print aobj


print "Wikipedia\n"
compare(congress,legs)

print "Legs\n"
compare(legs,congress)
