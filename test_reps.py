import os
#import socrata_rows as soc
import Current_members_of_the_United_States_House_of_Representatives as reps
import cache 
import urllib
import encode
import re 
from cStringIO import StringIO

rep= cache.cache('reps',reps.parse_rep)

def foo(link):
    link = urllib.unquote(link)
    link = re.search("/([^\/]+)$",link).group(1)          
    link = encode.decode(link)
#    print link
    return link

#print rep
for i in rep['names'].items() :
#    print i
    l= i[1]['link']
    l2 = foo(l)
#    print l2 


#print "REPS:",sorted(rep['wp'].keys())

