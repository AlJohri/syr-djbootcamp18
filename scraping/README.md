# scraping

## setup

```
brew install jq pup python3
pip3 install lxml
```

## scraping using `pup`

#### hackernews (https://news.ycombinator.com/)
```
curl -s https://news.ycombinator.com/ | pup 'table table tr:nth-last-of-type(n+2) td.title a.storylink json{}' | jq '.[] | {link: .href, text}'
```

#### songmeanings (https://songmeanings.com/popular/lyrics/)
```
curl -s 'https://songmeanings.com/popular/lyrics/' | pup 'table > tbody > tr json{}' | jq '.[] | {rank: .children[0].text, song: .children[1].children[0].text, delta: .children[2].children[0].text}'
```

## scraping using python3

- [imdb](./imdb.py) - http://www.imdb.com/chart/top
- [twitter](./twitter.py) - https://twitter.com/DataDhrumil
- [songmeanings](./songmeanings.py) - http://songmeanings.com/popular/lyrics/?chart=2018-05-04
