
fecelectronic:
	PYTHONPATH=./FECFieldDocumentation python fech.py '2009'

lint :
	~/.local/bin/pylint --output-format=parseable fec_electronic.py fec_electronic_contrib.py fecdetails.py fec.py fech_rendered_maps.py zipcsv.py fech.py fecfields.py cache.py fec_reports.py

flake :
	~/.local/bin/pyflakes  fec_electronic.py fec_electronic_contrib.py fecdetails.py fec.py fech_rendered_maps.py zipcsv.py fech.py fecfields.py cache.py fec_reports.py


feccontrib:
	python fec_electronic_contrib.py -f fec/880507.fec

fecd:
	python fecdetails.py

fec:
	python fec.py

getpages:
	python legis_getpages.py 

washpost_search : 
	python washpost_search.py

index_urls :
	python legis_index_links.py

washpost : 
	python washpost.py

test:
	python wikipedia_conglinks.py
