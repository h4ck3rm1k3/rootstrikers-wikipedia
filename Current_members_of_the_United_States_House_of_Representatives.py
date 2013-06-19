import lxml.html

def parse_rep() :
    reps = {}
    html = lxml.html.parse(
        "http://en.wikipedia.org/wiki/Current_members_of_the_United_States_House_of_Representatives?printable=yes"
        #    "http://en.wikipedia.org/w/index.php?title=List_of_current_United_States_Senators&printable=yes"
    )

    tables = html.xpath("//table")
    table = tables[1]
    for r in table.xpath("//tr") :
        data= r.xpath("td")
        if( len(data) == 10):
            f_district = data[1]
            f_image     = data[2]
            f_name     = data[3]
            (f_name_element, skip , f_name_link, skip) =f_name.iterlinks().next()
#            print "ele:%s" %  f_name_element.text
#            print "http://en.wikipedia.org" + f_name_link
            reps[f_name_element.text]= {
                'link' :   f_name_link
            }
    return reps

#parse_rep()
