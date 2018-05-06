# scraping

## setup

```
brew install jq pup python3
pip3 install lxml cssselect
```

## scraping using [`pup`](https://github.com/ericchiang/pup)

#### hackernews (https://news.ycombinator.com/)
```
curl -s https://news.ycombinator.com/ | pup 'table table tr:nth-last-of-type(n+2) td.title a.storylink json{}' | jq '.[] | {link: .href, text}'
```

#### songmeanings (https://songmeanings.com/popular/lyrics/)
```
curl -s 'https://songmeanings.com/popular/lyrics/' | pup 'table > tbody > tr json{}' | jq '.[] | {rank: .children[0].text, song: .children[1].children[0].text, delta: .children[2].children[0].text}'
```

## scraping using python3

#### imdb (http://www.imdb.com/chart/top)

```python
#!/usr/bin/env python3

import sys
import csv
import requests
import lxml.html

response = requests.get("http://www.imdb.com/chart/top")
doc = lxml.html.fromstring(response.content)

writer = csv.writer(sys.stdout)

for tr in doc.cssselect('.lister-list tr'):
    id = tr.cssselect('td.ratingColumn div[data-titleid]')[0].get('data-titleid')
    title = tr.cssselect('td.titleColumn a')[0].text
    rating = tr.cssselect('td.ratingColumn.imdbRating strong')[0].text
    writer.writerow([id, title, rating])
```

#### twitter (https://twitter.com/DataDhrumil)

```python
#!/usr/bin/env python3

import sys
import csv
import requests
import lxml.html

response = requests.get("https://twitter.com/datadhrumil")
doc = lxml.html.fromstring(response.content)

writer = csv.writer(sys.stdout)

for el in doc.cssselect("ol.stream-items > li.stream-item"):
	id = el.get('data-item-id')
	text = el.cssselect('.tweet-text')[0].text_content().strip()
	writer.writerow([id, text])
```

#### songmeanings (http://songmeanings.com/popular/lyrics/?chart=2018-05-04)

```python
#!/usr/bin/env python3

import sys
import csv
import requests
import lxml.html

response = requests.get("http://songmeanings.com/popular/lyrics/?chart=2018-05-04")
doc = lxml.html.fromstring(response.content)

writer = csv.writer(sys.stdout)

table = doc.cssselect("table[summary]")[0]
for item in table.cssselect("tbody > tr.item"):
    cells = item.getchildren()
    rank = cells[0].text_content().strip()
    title = cells[1].text_content().strip()
    margin = cells[2].text_content().strip()
    writer.writerow([rank, title, margin])
```

## scraping using [distill.io](https://distill.io/)


