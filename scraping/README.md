# scraping

## setup

```
brew install jq pup python3
pip3 install lxml cssselect xmltodict
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

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Modify the script above to get the

1) year each movie was made and
2) the number of users that rated the movie

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
    writer.writerow([rank, title])
```

### ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Try It

Modify the script above to get the delta +/- for each song and write the output

#### bioguide (http://bioguide.congress.gov/biosearch/biosearch.asp)

```python
#!/usr/bin/env python3

import sys
import csv
import requests
import lxml.html

response = requests.post("http://bioguide.congress.gov/biosearch/biosearch1.asp",
    data={"congress": "2018"})
doc = lxml.html.fromstring(response.content)

writer = csv.writer(sys.stdout)

for tr in doc.cssselect("center table tr"):
    if len(tr.cssselect('th')) > 0: continue

    cols = tr.cssselect("td")

    # only take first row of each legislator, not additional terms
    if not cols[0].cssselect("a"): continue

    name = cols[0].cssselect("a")[0].text
    birth_death = cols[1].text.replace('\xa0', '')
    position = cols[2].text
    party = cols[3].text
    state = cols[4].text
    congress = cols[5].text
    years = cols[5].cssselect('br')[0].tail.replace('(', '').replace(')', '')

    writer.writerow([name, birth_death, position, party, state, congress, years])
```

see [bioguide-complex.py](./bioguide-complex.py) for getting additional terms

#### syrairport (http://www.syrairport.org/)

```python3
#!/usr/bin/env python3

import sys
import csv
import requests
import xmltodict

response = requests.get("http://www.syrairport.org/flightdata/data.xml")
data = xmltodict.parse(response.text)

writer = csv.writer(sys.stdout)

for flight in data['flights']['flight']:

    date = flight['@date']
    claim = flight['@claim']
    remarks = flight['@remarks']
    gate = flight['@gate']
    actualtime = flight['@actualtime']
    scheduletime = flight['@scheduletime']
    city = flight['@city']
    flightnumber = flight['@flightnumber']
    airlinecode = flight['@airlinecode']
    indicator = flight['@indicator']
    type = flight['@type']

    writer.writerow([date, claim, remarks, gate, actualtime, scheduletime, city, flightnumber, airlinecode, indicator, type])
```

#### imdb episodes (https://www.imdb.com/title/tt3697842/episodes?season=1)

```python3
#!/usr/bin/env python3

import sys
import csv
import requests
import lxml.html

writer = csv.writer(sys.stdout)

for season in [1,2,3]:

    response = requests.get("https://www.imdb.com/title/tt3697842/episodes?season=1")
    doc = lxml.html.fromstring(response.content)

    for item in doc.cssselect('div.eplist .list_item'):
        episode_number = item.cssselect('meta[itemprop=episodeNumber]')[0].get('content')
        name = item.cssselect('a[itemprop=name]')[0].text
        link = item.cssselect('a[itemprop=name]')[0].get('href')
        writer.writerow([season, episode_number, name, link])
```

## scraping using [import.io](https://import.io/)

## scraping using [`pup`](https://github.com/ericchiang/pup)

#### hackernews (https://news.ycombinator.com/)
```
curl -s https://news.ycombinator.com/ | pup 'table table tr:nth-last-of-type(n+2) td.title a.storylink json{}' | jq '.[] | {link: .href, text}'
```

#### songmeanings (https://songmeanings.com/popular/lyrics/)
```
curl -s 'https://songmeanings.com/popular/lyrics/' | pup 'table > tbody > tr json{}' | jq '.[] | {rank: .children[0].text, song: .children[1].children[0].text, delta: .children[2].children[0].text}'
```

## notifications using [distill.io](https://distill.io/)
...and other services like "Klaxon". They all work the same way, once you know how to use CSS selectors (or x-path) you can use these services to get notified on specific web changes.
