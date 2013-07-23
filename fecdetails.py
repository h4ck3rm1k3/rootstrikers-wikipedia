import cache

def get(url, name):
    return cache.cacheweb(url)
    
get('ftp://ftp.fec.gov/FEC/2014/cm14.zip','Committee Master File')
get('ftp://ftp.fec.gov/FEC/2014/cn14.zip','Candidate Master File')
get('ftp://ftp.fec.gov/FEC/2014/ccl14.zip','Candidate Committee Linkage File')
get('ftp://ftp.fec.gov/FEC/2014/oth14.zip','Any Transaction from One Committee to Another')
get('ftp://ftp.fec.gov/FEC/2014/pas214.zip','Contributions to Candidates (and other expenditures) from Committees')
get('ftp://ftp.fec.gov/FEC/2014/indiv14.zip','Contributions by Individuals')
get('ftp://ftp.fec.gov/FEC/2014/add14.zip','Adds')
get('ftp://ftp.fec.gov/FEC/2014/chg14.zip','Changes')
get('ftp://ftp.fec.gov/FEC/2014/delete14.zip', 'Deletes')
