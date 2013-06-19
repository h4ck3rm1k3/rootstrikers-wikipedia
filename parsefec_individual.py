import csv
# description http://www.fec.gov/finance/disclosure/metadata/DataDictionaryContributionsbyIndividuals.shtml

# CMTE_ID
# 	Filer Identification Number
# 	1 	N 	VARCHAR2 (9 Byte)
# 	A 9-character alpha-numeric code assigned to a committee by the Federal Election Commission

# AMNDT_IND 	Amendment Indicator
# 	2 	Y 	VARCHAR2 (1 Byte)
# 	Indicates if the report being filed is new (N), an amendment (A) to a previous report, or a termination (T) report.

# RPT_TP 	Report Type
# 	3 	Y 	VARCHAR2 (3 Byte)
# 	Indicates the type of report filed. List of report type codes
# http://www.fec.gov/finance/disclosure/metadata/ReportTypeCodes.shtml

# TRANSACTION_PGI 	Primary-General Indicator
# 	4 	Y 	VARCHAR2 (5 Byte)
# 	This code indicates the election for which the contribution was made. EYYYY (election plus election year)
# P = Primary
# G = General
# O = Other
# C = Convention
# R = Runoff
# S = Special
# E = Recount

# IMAGE_NUM
# 	Microfilm Location (YYOORRRFFFF)
# 	5 	Y 	VARCHAR2 (11 Byte)
# 	Indicates the physical location of the filing.

# TRANSACTION_TP
# 	Transaction Type
# 	6 	Y 	VARCHAR2 (3 Byte)
# Transaction types 10, 11, 15, 15C, 15E, 15I, 15T, 19, 22Y, 24I, 24T, 20Y and 21Y are included in the INDIV file.
# For more information about transaction type codes see this list of transaction type codes
# http://www.fec.gov/finance/disclosure/metadata/DataDictionaryTransactionTypeCodes.shtml

# ENTITY_TP
# 	Entity Type
# 	7 	Y 	VARCHAR2 (3 Byte)
# 	CAN = Candidate
# CCM = Candidate Committee
# COM = Committee
# IND = Individual (a person)
# ORG = Organization (not a committee and not a person)
# PAC = Political Action Committee
# PTY = Party Organization

# NAME
# 	Contributor/Lender/Transfer Name
# 	8 	Y 	VARCHAR2 (200 Byte)
	 
# CITY
# 	City/Town
# 	9 	Y 	VARCHAR2 (30 Byte)
	 
# STATE
# 	State
# 	10 	Y 	VARCHAR2 (2 Byte)
	 
# ZIP_CODE
# 	Zip Code
# 	11 	Y 	VARCHAR2 (9 Byte)
	 
# EMPLOYER
# 	Employer
# 	12 	Y 	VARCHAR2 (38 Byte)
	 
# OCCUPATION
# 	Occupation
# 	13 	Y 	VARCHAR2 (38 Byte)
	 
# TRANSACTION_DT
# 	Transaction Date(MMDDYYYY)
# 	14 	Y 	DATE
	 
# TRANSACTION_AMT
# 	Transaction Amount
# 	15 	Y 	NUMBER (14,2)
	 
# OTHER_ID
# 	Other Identification Number
# 	16 	Y 	VARCHAR2 (9 Byte)
# 	For contributions from individuals this column is null. For contributions from candidates or other committees this column will contain that contributor's FEC ID.

# TRAN_ID
# 	Transaction ID
# 	17 	Y 	VARCHAR2 (32 Byte)
# 	ONLY VALID FOR ELECTRONIC FILINGS. A unique identifier permanently associated with each itemization or transaction appearing in an FEC electronic file.

# FILE_NUM
# 	File Number / Report ID
# 	18 	Y 	NUMBER (22)
# 	Unique report id

# MEMO_CD
# 	Memo Code
# 	19 	Y 	VARCHAR2 (1 Byte)
# 	'X' indicates that the amount is NOT to be included in the itemization total.

# MEMO_TEXT
# 	Memo Text
# 	20 	Y 	VARCHAR2 (100 Byte)
# 	A description of the activity. Memo Text is available on itemized amounts on Schedules A and B. These transactions are included in the itemization total.

# SUB_ID 	FEC Record Number 	21 	N 	NUMBER (19) 	Unique row ID 



fieldnames=[   
    'CMTE_ID','AMNDT_IND','RPT_TP','TRANSACTION_PGI','IMAGE_NUM','TRANSACTION_TP','ENTITY_TP','NAME','CITY','STATE','ZIP_CODE','EMPLOYER','OCCUPATION','TRANSACTION_DT','TRANSACTION_AMT','OTHER_ID','TRAN_ID', 'FILE_NUM','MEMO_CD', 'MEMO_TEXT',  'SUB_ID' ]

fec_dict_reader = csv.DictReader(open('ftp.fec.gov_FEC_2014_indiv14.txt'), delimiter='|', quotechar='"', restkey=100, fieldnames=fieldnames)
from collections import defaultdict
matrix = defaultdict(dict)
print fec_dict_reader.fieldnames

f = open("ftp.fec.gov_FEC_2014_indiv14.xml", 'w')
for line in fec_dict_reader:
    s = '{{fec row|year=2014|type=individual'
    for k in fieldnames :
        d = line[k]
    #    print k,":",d
        if (isinstance( d, int )):
            d= str(d)

        if d is not None and d != '\\N' and d != '':
            s = s + "|" + k + "=" + d

    s = s + '}}' + "\n"

    sutf8 = s.encode('UTF-8')
    f.write(sutf8)
