import unicodedata

def decode(link) :
    b = link
    link = unicode(link, 'utf-8')
    link = unicodedata.normalize('NFKD', link)
    return strip(link)

def decodeuc(link) :
    b = link
    link = unicode(link)
    link = unicodedata.normalize('NFKD', link)
    return strip(link)


def strip(link) :
    b = link

    link = link.encode('ascii','ignore')
    if (link  != b):
        print "Before %s After %s:" % (b, link)
    return link
