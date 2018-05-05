#!/usr/bin/env python3

import json
import requests
import lxml.html

response = requests.get("http://www.imdb.com/chart/top")
doc = lxml.html.fromstring(response.content)

for row in doc.cssselect('.lister-list tr'):
    id = row.cssselect('td.ratingColumn div[data-titleid]')[0].get('data-titleid')
    title = row.cssselect('td.titleColumn a')[0].text
    rating = row.cssselect('td.ratingColumn.imdbRating strong')[0].text
    print(json.dumps({"id": id, "title": title, "rating": rating}))
