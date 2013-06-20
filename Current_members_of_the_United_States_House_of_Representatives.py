import lxml.html
import urllib2
import os

def cache (url) :
    print url
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    url2=url
    url2=url2.replace("/","_")
    filename = "data/" + url2

    if not os.path.exists("data"):
        os.makedirs("data")

    if (os.path.exists(filename)):
        f =open(filename,'r')
        return f.read()
    else:
        r = urllib2.Request(url=url, headers=hdr     )
        d = urllib2.urlopen(r)
        data= d.read()
        f =open(filename,'w')
        f.write(data)
        return data


# <h2><span class="mw-headline" id="External_links">External links</span></h2>
# <ul>
# <li><a rel="nofollow" class="external text" href="http://keating.house.gov">Congressman William Keating official U.S. House site</a></li>
# <li><a rel="nofollow" class="external text" href="http://billkeating.org">Keating campaign website</a></li>
# <li><a rel="nofollow" class="external text" href="http://bioguide.congress.gov/scripts/biodisplay.pl?index=K000375">Biography</a> at the <i><a href="/wiki/Biographical_Directory_of_the_United_States_Congress" title="Biographical Directory of the United States Congress">Biographical Directory of the United States Congress</a></i></li>
# <li><a rel="nofollow" class="external text" href="http://www.votesmart.org/candidate/4743">Biography</a>, <a rel="nofollow" class="external text" href="http://www.votesmart.org/candidate/key-votes/4743">voting record</a>, and <a rel="nofollow" class="external text" href="http://www.votesmart.org/candidate/evaluations/4743">interest group ratings</a> at <a href="/wiki/Project_Vote_Smart" title="Project Vote Smart">Project Vote Smart</a></li>
# <li><a rel="nofollow" class="external text" href="http://www.govtrack.us/congress/person.xpd?id=412435">Congressional profile</a> at <a href="/wiki/GovTrack" title="GovTrack">GovTrack</a></li>
# <li><a rel="nofollow" class="external text" href="http://www.opencongress.org/people/show/412435_William_Keating">Congressional profile</a> at <a href="/wiki/Participatory_Politics_Foundation" title="Participatory Politics Foundation">OpenCongress</a></li>
# <li><a rel="nofollow" class="external text" href="http://herndon1.sdrdc.com/cgi-bin/can_detail/H0MA10082">Financial information (federal office)</a> at the <a href="/wiki/Federal_Election_Commission" title="Federal Election Commission">Federal Election Commission</a></li>
# <li><a rel="nofollow" class="external text" href="http://www.opensecrets.org/politicians/summary.php?cid=N00031933">Financial information (federal office)</a> at <a href="/wiki/Center_for_Responsive_Politics" title="Center for Responsive Politics">OpenSecrets.org</a></li>
# <li><a rel="nofollow" class="external text" href="http://www.legistorm.com/member/2826/Rep_Bill_Keating_MA.html">Staff salaries, trips and personal finance (federal office)</a> at LegiStorm.com</li>
# <li><a rel="nofollow" class="external text" href="http://www.ontheissues.org/MA/Bill_Keating.htm">Issue positions and quotes</a> at <a href="/wiki/On_the_Issues" title="On the Issues">On the Issues</a></li>
# <li><a rel="nofollow" class="external text" href="http://projects.washingtonpost.com/congress/members/K000375">Voting record</a> at <i><a href="/wiki/The_Washington_Post" title="The Washington Post">The Washington Post</a></i></li>
# <li><a rel="nofollow" class="external text" href="http://www.c-spanvideo.org/williamrkeating">Appearances</a> on <a href="/wiki/C-SPAN" title="C-SPAN">C-SPAN</a> programs</li>
# <li><a rel="nofollow" class="external text" href="http://www.worldcat.org/identities/np-keating,%20william%20r">Works by or about William R. Keating</a> in libraries (<a href="/wiki/WorldCat" title="WorldCat">WorldCat</a> catalog)</li>
# <li><a rel="nofollow" class="external text" href="http://www.nndb.com/people/993/000265198/">Entry</a> at <a href="/wiki/NNDB" title="NNDB">NNDB</a></li>
# </ul>


def parse_wiki_page_links(d):
    for (f_name_element, attr , f_link, pos) in d.iterlinks():
        print f_link

def parse_wiki_page(x) :
    d = cache ('http://en.wikipedia.org%s?printable=yes' % x)
    html = lxml.html.document_fromstring(
        d
    )
    parse_wiki_page_links(html)
    
def parse_rep() :
    reps = {}
#    d = cache ('http://en.wikipedia.org/wiki/Current_members_of_the_United_States_House_of_Representatives?printable=yes')
    d = cache ('http://en.wikipedia.org/wiki/Current_members_of_the_United_States_House_of_Representatives?printable=yes')
    html = lxml.html.document_fromstring(
        d
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

            (skip, skip , f_district_link, skip) =f_district.iterlinks().next()
#            print f_district_element, f_district_link
            (f_name_element, skip , f_name_link, skip) =f_name.iterlinks().next()
#            print "ele:%s" %  f_name_element.text
#            print "http://en.wikipedia.org" + f_name_link
            reps[f_name_element.text]= {
                'link' :   f_name_link,
                'district' :  f_district_link
            }
            parse_wiki_page(f_name_link)

    return reps

#parse_rep()
