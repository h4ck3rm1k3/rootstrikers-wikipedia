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

    with open("maplight-convert/active_incumbents.json") as infile:
        for line in infile:
            if 'person_id' in line:
                data = json.loads(line[:-2])
                full_name=data['display_name']
                sutf8 = full_name.encode('UTF-8')

                office = data['office_title']
                state = data['statecode']
                dist = data['district']
                party = data['party_name']

                if (party == 'Democrat-Farm-Labor') :
                    party = "Democratic"

                if office not in index:
                    index[office] = {}

                if state not in index[office]:
                    index[office][state] = {}

                if dist not in index[office][state]:
                    index[office][state][dist] = {}

                full_name = full_name.replace("\"","")
                full_name = full_name.replace("Mr. ","")
                full_name = full_name.replace("Mrs. ","")
                full_name = full_name.replace("Dr ","")
                full_name = full_name.replace("Hon. ","")
                
                if party not in index[office][state][dist]:
                    index[office][state][dist][party] = full_name                

    return index

data =parse()
import pprint
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint( data)


def person_match(full_name) :
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
    full_name2 =encode.decodeuc(nameobj['first'].lower() + " "+ nameobj['nick'].lower() + " "+   nameobj['last'].lower())
    if (full_name == last_obj):
        person_match(full_name)
        return True
    elif (full_name2 == last_obj):
        person_match(full_name2)
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
# remove mr. mrs. from name
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
        print "Fail last:\"%s\"" % last_obj, "name:",nameobj, "term:",last_term
        return False

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
            district=str(last_term['district'])
            if district == '0' :
                district ='1'

            #    print state

            if district in state_obj:

                district_obj = state_obj[ district ]

                party = last_term['party']
                if party == 'Democrat' :
                    party = 'Democratic'
                if party in district_obj :
                    last_obj = district_obj[ party ].lower()

                    check_simple(last_obj,nameobj)

                else:
                    print "missing ", party, "in district" , nameobj, last_term
                    pp.pprint( district_obj)
                    
            else:
                print "missing ", district, "in state", nameobj, last_term
                pp.pprint( state_obj)
        
#OrderedDict([('type', 'rep'), ('start', '2013-01-03'), ('end', '2015-01-03'), ('state', 'CA'), ('party', 'Democrat'), ('district', 19), ('url', 'http://www.house.gov/lofgren'), ('address', '1401 Longworth HOB; Washington DC 20515-0516'), ('phone', '202-225-3072'), ('fax', '202-225-3336'), ('contact_form', 'http://lofgren.house.gov/emailform.shtml'), ('office', '1401 Longworth House Office Building'), ('rss_url', 'http://lofgren.house.gov/index.php?format=feed&amp;type=rss')])

