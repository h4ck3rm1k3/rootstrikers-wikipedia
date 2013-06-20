# this data was retrieved from https://opendata.socrata.com/api/views/u2zt-jegr/rows.xml?accessType=DOWNLOAD
#from lxml import etree
import xml.etree.ElementTree as xml

def parse_socrata_rows () :
    res = {
        'names': {},
        'links': {},
    }
    tree = xml.parse("socrata_rows.xml")
    rootElement = tree.getroot()
    rows = rootElement.findall("row/row")
    for row in rows:
        name_middle=None

        obj = {}

        obj['_id']=row.get('id')
        obj['_uuid']=row.get('_uuid')
        obj['_position']=row.get('_position')
        obj['_address']=row.get('_address')

        name_first= row[0].text
        if row[3].text :
            if( row[3].tag == "middlename"):
                name_middle = row[3].text # middle name

        name_last = row[1].text 

        for data in row:
            obj[data.tag]=data.text

#        print name_first, name_middle, name_last


        if( name_middle):
            name = " " .join([name_first, name_middle, name_last])
        else:
            name = " " .join([name_first, name_last])
        if row[2].get('url') :
            url= row[2].get('url')

        obj['url'] = url
        obj['name'] = name
        obj['name_'] = name

# index the obj
        res['names'][name] = obj
        res['links'][url] = obj
        

        #print name
        
    return res
            #        print row[1].text
#        print row[2].text
#        print row[3].text
 #       for data in row.findall("firstname"):
 #           print data.tag, data.text
#        for data in row.findall("middlename"):
#            print data.tag, data.text
#        for data in row.findall("lastname"):
#            print data.tag, data.text


#res= parse_socrata_rows ()
#print res
