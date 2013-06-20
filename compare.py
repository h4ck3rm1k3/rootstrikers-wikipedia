import os
import socrata_rows as soc
import Current_members_of_the_United_States_House_of_Representatives as reps
import cache 
from cStringIO import StringIO



rep= cache.cache('reps',reps.parse_rep)
soc1= cache.cache('sox',soc.parse_socrata_rows)

for x in rep['links'].keys():
    repobj =     rep['links'][x]
    rep_name = repobj['name']
    if x in soc1['links'] :
        print "Found %s " % x
        print repobj
        print soc1['links'][x]
    else:
        if rep_name in soc1['names'] :
            print "Found %s " % rep_name
            print repobj
            print soc1['names'][rep_name]
        else:
            print "Missing %s " % x
            print repobj

