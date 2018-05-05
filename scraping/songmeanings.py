#!/usr/bin/env python3

import json
import requests
import lxml.html

response = requests.get("http://songmeanings.com/popular/lyrics/?chart=2018-05-04")
doc = lxml.html.fromstring(response.content)

table = doc.cssselect("table[summary]")[0]
for item in table.cssselect("tbody > tr.item"):
    cells = item.getchildren()
    rank = cells[0].text_content().strip()
    title = cells[1].text_content().strip()
    margin = cells[2].text_content().strip()
    print(json.dumps({"rank": rank, "title": title, "margin": margin}))
