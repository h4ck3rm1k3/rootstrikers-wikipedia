FECH reimplementation :

This contains fech.py, a rewrite of the fech project in python.
It uses a code generator for creating the record objects
 git@github.com:h4ck3rm1k3/FEC-Field-Documentation.git
which is checked out into FECFieldDocumentation

The results will be published here :
	git@github.com:h4ck3rm1k3/federal-election-commision-aggregation.git in
	the branch rawdata


CRP_IDs.txt 
-----------

Source :
Open Secrets http://www.opensecrets.org/
Data file here :http://www.opensecrets.org/downloads/crp/CRP_IDs.xls

contains basic data about  the Candidate and connects the FECID to to CID.
Uploaded to google docs.
https://docs.google.com/spreadsheet/ccc?key=0AoQovvVR7xyxdFhMVlhvUHdRSXR5V1dHXzZuM3JaOUE#gid=0

Maplight 
---------
The site http://maplight.org/ has a data api. It pulls in FEC data. 

Example :
{"display_name":"Barack Obama","statecode":"US","office_body":"E","office_title":"President","district":"","district_sort":"","party_name":"Democratic","description":"57th Administration","start_date":"2013-01-20","end_date":"2017-01-20","sworn_in":"2013-01-20","person_id":"7258"},

This is from http://data.maplight.org/FEC/active_incumbents.json

Example data: http://data.maplight.org/FEC/2012/summaries/all.json or from 2014 :http://data.maplight.org/FEC/2014/summaries/all.json

Here is an example from 2012 :
{"person_id":"7258","last_name":"Obama","first_name":"Barack","full_name":"Barack Obama","gender":"M","party":"Democratic","state":"US","office_running":"President","district_running":"","ico":"I","status":"Won","status_date":"Nov 6, 2012","office_holding":null,"district_holding":null,"contrib_start":"Jan 1, 2011","contrib_end":"Jun 23, 2013","contrib_total":"722309354","url_photo":"http:\/\/images.maplight.org\/persons\/7258.jpg","top_orgs":{"1":{"name":"U.S. Government","total":"2887185"},"2":{"name":"University of California","total":"1000166"},"3":{"name":"Microsoft","total":"641217"},"4":{"name":"Google","total":"591093"},"5":{"name":"Kaiser Permanente","total":"563238"},"6":{"name":"Harvard University","total":"510130"},"7":{"name":"Stanford University","total":"390581"},"8":{"name":"DLA Piper","total":"354834"},"9":{"name":"Columbia University","total":"339650"},"10":{"name":"Sidley Austin","total":"338490"},"11":{"name":"Deloitte","total":"322016"},"12":{"name":"Comcast","total":"271545"},"13":{"name":"University of Chicago","total":"260746"},"14":{"name":"International Business Machines","total":"254220"},"15":{"name":"JPMorgan Chase","total":"244382"},"16":{"name":"Apple","total":"237143"},"17":{"name":"Disney","total":"236660"},"18":{"name":"Skadden, Arps, Slate, Meagher & Flom","total":"233183"},"19":{"name":"University of Michigan","total":"232744"},"20":{"name":"Time Warner","total":"228751"}},"all_count":"2133","all_rank":"1","chamber_count":"116","chamber_rank":1},

The IDs from maplight can be seen in the image urls html : data.maplight.org/FEC/2012/summaries/all.html, The ids are not usable directly on the front end.
