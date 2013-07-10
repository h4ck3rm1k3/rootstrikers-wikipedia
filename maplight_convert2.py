import re
import json
import encode
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

                office = data['office_holding']
                state = data['state']
                dist = data['district_holding']
                party = data['party']
                
                if office not in index:
                    index[office] = {}

                if state not in index[office]:
                    index[office][state] = {}

                if dist not in index[office][state]:
                    index[office][state][dist] = {}

                if party not in index[office][state][dist]:
                    index[office][state][dist][party] = full_name                
    return index

data =parse()
import pprint
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint( data)


def person_match(full_name) :
    print "match",full_name
    pass

def check_suffix(old_name,last_obj,nameobj):
    if 'suffix' in nameobj :
        full_name = old_name + " " + nameobj['suffix'].lower()
        if ( full_name == last_obj) :
            #print "match5!",full_name
            person_match(full_name)
            return True
        else:
            return False

def check_middle_initial (last_obj,nameobj): 
    full_name =encode.decodeuc(nameobj['first'].lower() + " "+ nameobj['middle'][0].lower() + ". "+   nameobj['last'].lower())
    if (full_name == last_obj) :
#        print "match!",full_name
        person_match(full_name)
        return True

    else:
        return check_suffix(full_name,last_obj,nameobj)


def check_nick (last_obj,nameobj): 
    full_name =encode.decodeuc(nameobj['nick'].lower() + " "+   nameobj['last'].lower())
    if (full_name == last_obj) :
#        print "match6!",full_name
#        return True
        person_match(full_name)
        return True

    else:
        return check_suffix(full_name,last_obj,nameobj)

def check_middle (last_obj,nameobj): 
    full_name =encode.decodeuc(nameobj['first'].lower() + " "+  nameobj['middle'].lower() + " "+  nameobj['last'].lower())
    if (full_name == last_obj) :
#        print "match3!",full_name
        person_match(full_name)
        return True

    else :
        if (not check_middle_initial(last_obj,nameobj)) :
            return check_suffix(full_name,last_obj,nameobj)

## todo 
# 1. prefix (dr.)
# middle names without .
# alt names (double last names, try both)
# remove " from name
# last, first

def check_simple(last_obj,nameobj):
    full_name =encode.decodeuc(nameobj['official_full'].lower())
    full_name2 =encode.decodeuc(nameobj['first'].lower() + " "+ nameobj['last'].lower())
    if (full_name == last_obj) :
        person_match(full_name)
        return True
    elif (full_name2 == last_obj) :
        person_match(full_name)
        return True
    elif 'nick' in nameobj :
        return check_nick(last_obj,nameobj)
    elif 'middle' in nameobj :
        return check_middle(last_obj,nameobj)
    else:
#        print "last",last_obj,"name",nameobj,"term",last_term
        return False

def scan_district (state_obj,nameobj):
    for district in state_obj:
        district_obj = state_obj[ district ]
#        party = last_term['party']
#        if party == 'Democrat' :
#            party = 'Democratic'
        for party in district_obj :
            last_obj = district_obj[ party ].lower()
            if check_simple(last_obj,nameobj):
                return True
#        else:
#            print "missing ", party, "in district" , nameobj
#            pp.pprint( district_obj)

for x in sorted(legs['wp'].keys()):
    last_term = legs['wp'][x]['terms'][-1]
    nameobj= legs['wp'][x]['name'] 
    if (last_term['type'] == 'rep'):
        chamber= data['House']
    else:
        chamber= data['Senate']
    state=last_term['state']
    if (state in chamber ) :

        state_obj = chamber [ state ] 

        if 'district' in last_term :
            #    print state
#            for district in [str(last_term['district']),str(last_term['district'] +1),str(last_term['district'] -1)] :
            scan_district(state_obj,nameobj)

#OrderedDict([('type', 'rep'), ('start', '2013-01-03'), ('end', '2015-01-03'), ('state', 'CA'), ('party', 'Democrat'), ('district', 19), ('url', 'http://www.house.gov/lofgren'), ('address', '1401 Longworth HOB; Washington DC 20515-0516'), ('phone', '202-225-3072'), ('fax', '202-225-3336'), ('contact_form', 'http://lofgren.house.gov/emailform.shtml'), ('office', '1401 Longworth House Office Building'), ('rss_url', 'http://lofgren.house.gov/index.php?format=feed&amp;type=rss')])

