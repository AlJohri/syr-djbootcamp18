
```
brew install jq pup
```

```
curl -s https://news.ycombinator.com/ | pup 'table table tr:nth-last-of-type(n+2) td.title a.storylink json{}' | jq '.[] | {link: .href, text}'
```