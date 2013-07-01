#!/usr/bin/python
import os
import legislators_current as leg
import legislators_other as leg2

import dump
import cache 

from cStringIO import StringIO
legs= leg.load()
legs2= leg2.load()

def compare(a,b) :
    for x in sorted(a['wp'].keys()):
        aobj = a['wp'][x]
        bobj = b['wp'][x]
        if 'maplight'  in aobj['id'] :
            ml = aobj['id']['maplight']
            bobj['id']['maplight']=ml
                        
compare(legs,legs2)
leg.apply(legs)
dump.dump(legs2)
