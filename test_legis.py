import os
import legislators_current as leg
import cache 
import urllib
import encode
import re 
from cStringIO import StringIO

legs= leg.load()
#print legs
#for i in legs.keys() :
#    print i
#    n= i[1]['name']
#    n2 = encode.decode(n)
#    print n,n2,i


print "REPS:",sorted(legs['wp'].keys())

