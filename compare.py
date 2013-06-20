import socrata_rows as soc
import Current_members_of_the_United_States_House_of_Representatives as reps

rep= reps.parse_rep()
soc1= soc.parse_socrata_rows ()

for x in rep.keys():
    if x in soc1 :
        print rep[x]
        print soc1[x]
    else:
        print "Missing %s " % x
