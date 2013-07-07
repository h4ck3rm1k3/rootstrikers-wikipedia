import re
import json
import encode
import dump
from pprint import pprint
import legislators_current as leg
legs= leg.load()
 
"""
we just read in the maplight data and the current legislators and the add in the maplight name as well.
"""

fields = [ 'district_holding', 'district_running',
           'first_name', 'full_name', 'gender', 'ico', 'last_name', 'office_holding',
           'office_running', 'party', 'person_id', 'state', 'status', 'status_date',           'url_photo' ]

def parse():
    index= {    };
    with open("maplight-convert/active_incumbents.json") as infile:
        for line in infile:
            if 'person_id' in line:
                data = json.loads(line[:-2])
                person_id =str(data['person_id'] )
#                print person_id                , data
                index[person_id]= data['display_name']#data
            else:
                print line
    return index

data =parse()
#print data

for x in sorted(legs['wp'].keys()):
    idsobj= legs['wp'][x]['id'] 
    
    if 'maplight' in idsobj:
        maplight_id = str(idsobj['maplight'])
        if maplight_id in data :
#            print "foun",maplight_id
            mp=data[maplight_id]
            idsobj['maplight_name']=mp
        else:
#            pass
            print "missing",maplight_id
leg.apply(legs)
dump.dump(legs)
