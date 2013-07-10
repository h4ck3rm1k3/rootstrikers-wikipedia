import csv
import string 
import legislators_current as leg
import dump
fecs = {}
legs= leg.load()
for x in sorted(legs['wp'].keys()):
    obj= legs['wp'][x]
    idsobj= obj['id'] 
    name = obj['name']['official_full'] 
    if 'fec' in idsobj:
        for fec in idsobj['fec']:
#            print "fec",fec
            fecs[fec]=obj

filename= "maplight-convert/FEC2012c1_1.csv"
fieldnames=[   "TransactionTypeCode","TransactionType","ElectionCycle","ReportingCommitteeMLID","ReportingCommitteeFECID","ReportingCommitteeName","ReportingCommitteeNameNormalized","PrimaryGeneralIndicator","TransactionID","FileNumber","RecordNumberML","RecordNumberFEC","TransactionDate","TransactionAmount","RecipientName","RecipientNameNormalized","RecipientCity","RecipientState","RecipientZipCode","RecipientEmployer","RecipientEmployerNormalized","RecipientOccupation","RecipientOccupationNormalized","RecipientOrganization","RecipientEntityTypeCode","RecipientEntityType","RecipientCommitteeMLID","RecipientCommitteeFECID","RecipientCommitteeName","RecipientCommitteeNameNormalized","RecipientCommitteeTreasurer","RecipientCommitteeDesignationCode","RecipientCommitteeDesignation","RecipientCommitteeTypeCode","RecipientCommitteeType","RecipientCommitteeParty","RecipientCandidateMLID","RecipientCandidateFECID","RecipientCandidateName","RecipientCandidateNameNormalized","RecipientCandidateParty","RecipientCandidateICO","RecipientCandidateStatus","RecipientCandidateOfficeState","RecipientCandidateOffice","RecipientCandidateDistrict","RecipientCandidateGender","DonorName","DonorNameNormalized","DonorCity","DonorState","DonorZipCode","DonorEmployer","DonorEmployerNormalized","DonorOccupation","DonorOccupationNormalized","DonorOrganization","DonorEntityTypeCode","DonorEntityType","DonorCommitteeMLID","DonorCommitteeFECID","DonorCommitteeName","DonorCommitteeNameNormalized","DonorCommitteeTreasurer","DonorCommitteeDesignationCode","DonorCommitteeDesignation","DonorCommitteeTypeCode","DonorCommitteeType","DonorCommitteeParty","DonorCandidateMLID","DonorCandidateFECID","DonorCandidateName","DonorCandidateNameNormalized","DonorCandidateParty","DonorCandidateICO","DonorCandidateStatus","DonorCandidateOfficeState","DonorCandidateOffice","DonorCandidateDistrict","DonorCandidateGender","UpdateTimestamp" ]

fec_dict_reader = csv.DictReader(open(filename), delimiter=',', quotechar='"', restkey=100, fieldnames=fieldnames)
from collections import defaultdict
matrix = defaultdict(dict)
#print fec_dict_reader.fieldnames

f = open(filename + ".xml", 'w')
for line in fec_dict_reader:
    for k in fieldnames :
        d = line[k]
        if (isinstance( d, int )):
            d= str(d)
        if d is not None  and d != '':           
            if string.find(k,"FECID") > 0:
                #print  k + "=" + d                
                val = line['TransactionAmount']
                if (val == 'TransactionAmount'):
                    continue
                if (len(val)> 0):
                    try:
                        val = int(val)
                    except:
                        print val, "failed"
                else:
                    val = 0
                    
                name = line['DonorName']
                if d not in fecs:
                    fecs[d]= {}
                    fecs[d]["fec_2012_1total"] ={ } 
                    fecs[d]["fec_2012_1total"][name] = val                  
                else:
                    if "fec_2012_1total" in fecs[d]:
                        if name in fecs[d]["fec_2012_1total"]:
                            fecs[d]["fec_2012_1total"][name] = fecs[d]["fec_2012_1total"][name] + val 
                        else:
                            fecs[d]["fec_2012_1total"] ={ } 
                            fecs[d]["fec_2012_1total"][name] = val                  
                    else:
                        fecs[d]["fec_2012_1total"] ={ } 

dump.dump_data(fecs)
