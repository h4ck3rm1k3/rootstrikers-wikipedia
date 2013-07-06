import re
import json
import encode
import dump
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
                person_id = data['person_id']

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
                    index[office][state][dist][party] = []
                index[office][state][dist][party].append( { 'name' :  full_name,'id' :  int(person_id)  })


    return index

data =parse()
import pprint
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint( data)


def person_match(full_name) :
    #print "Matched %s" % full_name
    return True


def check_suffix(old_name,maplight_name,nameobj):
    if 'suffix' in nameobj :
        suffix = nameobj['suffix'].lower()
        full_name = old_name + " " + suffix
        suffix = suffix.replace(".", "")
        full_name2 = old_name + " " + suffix
        if ( full_name == maplight_name) :
            return person_match(full_name)
        elif ( full_name2 == maplight_name) :
            return person_match(full_name)

        else:
            return False

def check_middle_initial (maplight_name,nameobj): 
    full_name =encode.decodeuc(nameobj['first'].lower() + " "+ nameobj['middle'][0].lower() + ". "+   nameobj['last'].lower())
    full_name2 =encode.decodeuc(nameobj['first'].lower() + " "+ nameobj['middle'][0].lower() + " "+   nameobj['last'].lower())

    if (full_name == maplight_name) :
        return person_match(full_name)

    elif (full_name2 == maplight_name) :
        return person_match(full_name)

    elif check_suffix(full_name,maplight_name,nameobj) :
        return person_match(full_name)

    else :
        return check_suffix(full_name2,maplight_name,nameobj)
    return False

def check_nick (maplight_name,nameobj): 

    full_name =encode.decodeuc(nameobj['nick'].lower() + " "+   nameobj['last'].lower())
    full_name2 =encode.decodeuc(nameobj['first'].lower() + " "+ nameobj['nick'].lower() + " "+   nameobj['last'].lower())
    if (full_name == maplight_name):
        return person_match(full_name)

    elif (full_name2 == maplight_name):
        return person_match(full_name2)

    else:
        return check_suffix(full_name,maplight_name,nameobj)


def check_middle (maplight_name,nameobj): 
    full_name =encode.decodeuc(nameobj['first'].lower() + " "+  nameobj['middle'].lower() + " "+  nameobj['last'].lower())
    if (full_name == maplight_name) :
#        print "match3!",full_name
        return person_match(full_name)


    else :
        if (not check_middle_initial(maplight_name,nameobj)) :
            return check_suffix(full_name,maplight_name,nameobj)

    return False

## todo 
# 1. prefix (dr.)
# middle names without .
# alt names (double last names, try both)
# remove " from name
# remove mr. mrs. from name
# last, first

def check_simple(maplight_name,nameobj):
    full_name =encode.decodeuc(nameobj['official_full'].lower())
    full_name2 =encode.decodeuc(nameobj['first'].lower() + " "+ nameobj['last'].lower())
    if (full_name == maplight_name) :
        return person_match(full_name)

    elif (full_name2 == maplight_name) :
        return person_match(full_name)

    elif 'nick' in nameobj :
        return check_nick(maplight_name,nameobj)
    elif 'middle' in nameobj :
        return check_middle(maplight_name,nameobj)
    else:
#        print "Fail last:\"%s\"" % maplight_name, "name:",nameobj
        return False

def scan_all(x):
    last_term = legs['wp'][x]['terms'][-1]
    nameobj= legs['wp'][x]['name'] 
    idsobj= legs['wp'][x]['id'] 

    for chamber in  data.keys():
        chamber_obj =data[chamber]
        for state in chamber_obj.keys():
            state_obj = chamber_obj [ state ] 
            for district in state_obj .keys():
                district_obj = state_obj[ district ]
                for party in district_obj.keys() :
                    for candidate in district_obj[ party ] :
                        maplight_name = candidate['name'].lower()
                        maplight_id = candidate['id']
                        x = x.replace("_(U.S._politician)",'')
                        x = x.replace("_"," ")
                        x = x.lower()
                        #print maplight_name,x
                        if (maplight_name == x) :
                            idsobj['maplight']=maplight_id
                            return maplight_id
                        if check_simple(maplight_name,nameobj):
                            idsobj['maplight']=maplight_id
                            return maplight_id
    return None


def std_match(x):
    last_term = legs['wp'][x]['terms'][-1]
    nameobj= legs['wp'][x]['name'] 
    idsobj= legs['wp'][x]['id'] 

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
                    maplight_name = district_obj[ party ]['name'].lower()
                    maplight_id = district_obj[ party ]['id']
                    if (maplight_name == x) :
                        idsobj['maplight']=maplight_id

                    if check_simple(maplight_name,nameobj):
                        idsobj['maplight']=maplight_id
#                        print "new id",maplight_id
                    else: 
                        print "failed ",maplight_name,"|",nameobj['official_full']#, last_term
                        idsobj['maplight']=maplight_id

                else:
                    print "missing ", party, "in district" , nameobj, last_term
                    pp.pprint( district_obj)
                    
            else:
                print "missing ", district, "in state", nameobj, last_term
                pp.pprint( state_obj)
    else:
        print "missing state", state, "in state", nameobj, last_term
        pp.pprint( chamber)

def match_maplight(x):
    last_term = legs['wp'][x]['terms'][-1]
    nameobj= legs['wp'][x]['name'] 
    idsobj= legs['wp'][x]['id'] 
    if 'maplight' in idsobj :
        #print x,idsobj['maplight']
        return
    print "Still missing", x
    newid = scan_all(x)
    if newid == None:
        print "Could not find", x
    else:
        print "New id", newid
        

        
for x in sorted(legs['wp'].keys()):
    match_maplight(x)
#OrderedDict([('type', 'rep'), ('start', '2013-01-03'), ('end', '2015-01-03'), ('state', 'CA'), ('party', 'Democrat'), ('district', 19), ('url', 'http://www.house.gov/lofgren'), ('address', '1401 Longworth HOB; Washington DC 20515-0516'), ('phone', '202-225-3072'), ('fax', '202-225-3336'), ('contact_form', 'http://lofgren.house.gov/emailform.shtml'), ('office', '1401 Longworth House Office Building'), ('rss_url', 'http://lofgren.house.gov/index.php?format=feed&amp;type=rss')])

leg.apply(legs)
dump.dump(legs)
