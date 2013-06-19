#from lxml import etree
import xml.etree.ElementTree as xml

def parse_socrata_rows () :
    res = {}
    tree = xml.parse("socrata_rows.xml")
    rootElement = tree.getroot()
    rows = rootElement.findall("row/row")
    for row in rows:
        name_middle=None
#        print "\nROW\n"
        #for data in row:
        name_first= row[0].text
        if row[3].text :
            if( row[3].tag == "middlename"):
                name_middle = row[3].text # middle name

        name_last = row[1].text 

#        print name_first, name_middle, name_last
        if( name_middle):
            name = " " .join([name_first, name_middle, name_last])
        else:
            name = " " .join([name_first, name_last])
        if row[2].get('url') :
            url= row[2].get('url')

        res[name] = url
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
