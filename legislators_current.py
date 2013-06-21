import yaml
import cache


def loadlegis ():
    legis = yaml.load(file('congress-legislators/legislators-current.yaml', 'rb').read())
    return legis

def load():
    data = {
        'wp' : {} 
    }
    legis = cache.cache ( "legis",loadlegis)
    for l in legis:
        if 'wikipedia' in l['id'] :
            wp = l['id']['wikipedia']
            wp = wp.replace(" ","_")
#            wp = wp.decode("utf8")
#            wp=wp.encode('ascii', 'ignore')
            data['wp'][wp]=l
    return data

#print legis
#print legis.keys
