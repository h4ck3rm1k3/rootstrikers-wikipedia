import yaml
import cache
import encode
import codecs

def loadlegis ():
    filename ='congress-legislators/legislators-current.yaml'
    f = codecs.open(filename, "rb", "utf-8")
    data = f.read()
    legis = yaml.load(data)
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
            wp = encode.decodeuc(wp)
            data['wp'][wp]=l
    return data

#print legis
#print legis.keys
