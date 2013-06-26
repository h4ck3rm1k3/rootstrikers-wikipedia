import yaml
import cache

from yaml import CSafeLoader as Loader, CDumper as Dumper

def construct_odict(load, node):
    omap = OrderedDict()
    yield omap
    if not isinstance(node, yaml.MappingNode):
        raise yaml.constructor.ConstructorError(
            "while constructing an ordered map",
            node.start_mark,
            "expected a map, but found %s" % node.id, node.start_mark
        )
    for key, value in node.value:
        key = load.construct_object(key)
        value = load.construct_object(value)
        omap[key] = value

Loader.add_constructor(u'tag:yaml.org,2002:map', construct_odict)

def loadlegis ():

    legis = yaml.load(file('congress-legislators/legislators-current.yaml', 'rb').read(),Loader=Loader)
    return legis

def load():
    legis = cache.cache ( "legis",loadlegis)
    data = {        'raw' : legis    }

    for l in legis:
        if 'wikipedia' in l['id'] :
            wp = l['id']['wikipedia']
            data[wp]=l
        else:
            warn  "no wikipedia ", l 

    return data

def apply(data):
    for l in data['raw'] :
        if 'wikipedia' in l['id'] :
            wp = l['id']['wikipedia']
            new = data[wp]
            l['id']=new['id']
    return data

#print legis
#print legis.keys
