#!/usr/bin/env python3

import json
import requests
import lxml.html

response = requests.get("https://twitter.com/datadhrumil")
doc = lxml.html.fromstring(response.content)

for el in doc.cssselect("ol.stream-items > li.stream-item"):
	id = el.get('data-item-id')
	text = el.cssselect('.tweet-text')[0].text_content().strip()
	print(json.dumps({"id": id, "text": text}))
