import yaml
import cache

def loadlegis ():
    legis = yaml.load(file('congress-legislators/legislators-current.yaml', 'rb').read())
    return legis

legis = cache.cache ( "legis",loadlegis)
#print legis
#print legis.keys
for l in legis:
    #['bio', 'terms', 'id', 'name']
#    print l['bio']
    if 'wikipedia' in l['id'] :
#        print l['id']]
        pass
    else:
        print l
        
