import re
import json
from pprint import pprint
import legislators_current as leg
legs= leg.load()

fields = [ 'district_holding', 'district_running',
           'first_name', 'full_name', 'gender', 'ico', 'last_name', 'office_holding',
           'office_running', 'party', 'person_id', 'state', 'status', 'status_date',           'url_photo' ]

def parse():

    index= {

    };

    with open("maplight-convert/all_split.json") as infile:
        for line in infile:
            if 'person_id' in line:
                if(line[-1] == ']'):
                    data = json.loads(line[:-1])
                else:
                    data = json.loads(line[:-2])
                full_name=data['full_name']
                sutf8 = full_name.encode('UTF-8')

                office_running = data['office_running']
                state = data['state']
                dist = data['district_running']
                party = data['party']
                
                if office_running not in index:
                    index[office_running] = {}

                if state not in index[office_running]:
                    index[office_running][state] = {}

                if dist not in index[office_running][state]:
                    index[office_running][state][dist] = {}

                if party not in index[office_running][state][dist]:
                    index[office_running][state][dist][party] = full_name

                
    return index

data =parse()
import pprint
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint( data)

for x in sorted(legs['wp'].keys()):
    last_term = legs['wp'][x]['terms'][-1]

    if (last_term['type'] == 'rep'):
        chamber= data['House']
    else:
        chamber= data['Senate']

    state=last_term['state']

    if (state in chamber ) :

        state_obj = chamber [ state ] 

        if 'district' in last_term :
            district=str(last_term['district'])
            #    print state
            if district in state_obj:
                district_obj = state_obj[ district ]

                party = last_term['party']
                if party == 'Democrat' :
                    party = 'Democratic'
                if party in district_obj :
                    last_obj = district_obj[ party ]

                    full_name =legs['wp'][x]['name']['official_full']
                    full_name2 =legs['wp'][x]['name']['first'] + " "+ legs['wp'][x]['name']['last']

                    if (full_name == last_obj) :
                        print "match!",full_name
                    elif (full_name2 == last_obj) :
                        print "match2!",full_name
                    elif 'middle' in legs['wp'][x]['name'] :
                        full_name3 =legs['wp'][x]['name']['first'] + " "+ legs['wp'][x]['name']['middle'] + " "+ legs['wp'][x]['name']['last']
                        if (full_name3 == last_obj) :
                            print "match2!",full_name
                        else:
                            print "last",last_obj
                            print "name",legs['wp'][x]['name']
                            print "term",last_term
                    else:
                        print "last",last_obj
                        print "name",legs['wp'][x]['name']
                        print "term",last_term

                else:
                    print "missing ", party, "in district"
                    pp.pprint( district_obj)
                    
            else:
                print "missing ", district, "in state"
                pp.pprint( state_obj)
        
#OrderedDict([('type', 'rep'), ('start', '2013-01-03'), ('end', '2015-01-03'), ('state', 'CA'), ('party', 'Democrat'), ('district', 19), ('url', 'http://www.house.gov/lofgren'), ('address', '1401 Longworth HOB; Washington DC 20515-0516'), ('phone', '202-225-3072'), ('fax', '202-225-3336'), ('contact_form', 'http://lofgren.house.gov/emailform.shtml'), ('office', '1401 Longworth House Office Building'), ('rss_url', 'http://lofgren.house.gov/index.php?format=feed&amp;type=rss')])

