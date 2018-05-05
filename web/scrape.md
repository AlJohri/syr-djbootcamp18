
```
brew install jq pup
```

#### hackernews (https://news.ycombinator.com/)
```
curl -s https://news.ycombinator.com/ | pup 'table table tr:nth-last-of-type(n+2) td.title a.storylink json{}' | jq '.[] | {link: .href, text}'
```

#### songmeanings (https://songmeanings.com/popular/lyrics/)
```
curl 'https://songmeanings.com/popular/lyrics/' | pup 'table > tbody > tr json{}' | jq '.[] | {rank: .children[0].text, song: .children[1].children[0].text, margin: .children[2].children[0].text}'
```
