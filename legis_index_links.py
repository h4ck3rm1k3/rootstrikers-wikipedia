import os
import legislators_current as leg
import cache 
import urllib
import encode
import re 
from cStringIO import StringIO

"""

this will index the phone numbers and websites to find the legislators
we can use that to look for links in the washpost pages by url or phone.

"""
legs= leg.load()

contacts={}

def index(n,term,target_field,field_list):
    for field_name in field_list :
        if field_name in term :
            if target_field not in contacts:
                contacts[target_field]={}
            v=term[field_name]
            v = v.rstrip("/")
            if v in contacts[target_field]:
                n2=contacts[target_field][v]
                if not n == n2 :
                    print "error",v,n,n2,field_name,target_field
            else:
                contacts[target_field][v]=n
            
            
for x in sorted(legs['wp'].keys()):
    for t in legs['wp'][x]['terms']:
#        index(x,t,'url',['contact_form'])
        index(x,t,'url',['contact_form','url'])
        index(x,t,'phone',['phone','fax'] )

    
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(contacts)

#print 
