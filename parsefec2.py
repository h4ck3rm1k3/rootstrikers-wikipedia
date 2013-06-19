import csv
#fec_reader = csv.reader(open('data.csv'))
#or
fec_dict_reader = csv.DictReader(open('data.csv'), delimiter=',', quotechar='"')
from collections import defaultdict
matrix = defaultdict(dict)
f = open("data.xml", 'w')
for line in fec_dict_reader:
    s = '{{fec row|'
    for k in line.keys() :
        d = line[k]
        if (isinstance( d, int )):
            d= str(d)
        if d is None:
            next
        if d == '\\N':
            next
        else:
            s = s + "|" + k + "=" + d
    s = s + '}}' + "\n"
    print s
    sutf8 = s.encode('UTF-8')
    f.write(sutf8)
