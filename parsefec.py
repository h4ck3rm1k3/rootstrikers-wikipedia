import csv
#fec_reader = csv.reader(open('data.csv'))
#or
fec_dict_reader = csv.DictReader(open('data.csv'), delimiter=',', quotechar='"')
from collections import defaultdict
matrix = defaultdict(dict)

for line in fec_dict_reader:
    amnt = int(line["TransactionAmount"])

    if (amnt <  0) :
        print amnt, line

    if not (    line['RecipientState'] in   matrix         and         line['DonorState'] in matrix [  line['RecipientState']   ]    ) :
        matrix [ line['RecipientState']    ][  line['DonorState'] ] = 0
        
    matrix [  line['RecipientState']    ][ line['DonorState'] ] += amnt



for receipt in sorted(matrix.keys()):
    print receipt
    for send in sorted(matrix[receipt].keys()):
        v = matrix [receipt][send ] 
        print receipt, send,v
