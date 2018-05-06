#!/usr/bin/env python3

import json
import requests
import lxml.html

response = requests.post("http://bioguide.congress.gov/biosearch/biosearch1.asp", data={"congress": 2018})
doc = lxml.html.fromstring(response.content)

legislators = []
current_legislator = None

for tr in doc.cssselect("center table tr"):
	cols = tr.cssselect("td")
	if not cols: continue

	if cols[0].cssselect("a"):

		if current_legislator:
			legislators.append(current_legislator)

		current_legislator = {
			"name": cols[0].cssselect("a")[0].text,
			"link": cols[0].cssselect("a")[0].get('href'),
			"birth_death": cols[1].text.replace('\xa0', ''),
			"terms": []
		}

		term = {
			"position": cols[2].text,
			"party": cols[3].text,
			"state": cols[4].text,
			"congress": cols[5].text,
			"years": cols[5].cssselect('br')[0].tail.replace('(', '').replace(')', '')
		}

		current_legislator['terms'].append(term)

	else:

		term = {
			"position": cols[2].text,
			"party": cols[3].text,
			"state": cols[4].text,
			"congress": cols[5].text,
			"years": cols[5].cssselect('br')[0].tail.replace('(', '').replace(')', '')
		}

		current_legislator['terms'].append(term)

print(json.dumps(legislators, indent=4))
