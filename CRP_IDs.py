import csv

def parse() :
    fec = {}
    data = list(csv.reader(open('CRP_IDs.txt', 'rb'), delimiter='\t'))
    for d in data:
#        print d
        obj = {
            'CID': d[0],
            'CRPName':d[1],
            'Party':d[2],
            'DistIDRunFor':d[3],
            'FECCandID' :d[4]
        }
        fec [obj['FECCandID']]=obj
    return fec

#print parse();
