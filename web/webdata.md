# Unpacking Websites & Hunting for Data

This session will involve opening up chrome's developer tools in the browser to see how websites are structured. We will also go through some examples of how to extract data from websites, how to find data behind a chart if it is on the page, and how to discover hidden or undocumented APIs. Some examples will be drawn from previous FiveThirtyEight stories.

## Setup

### Install Chrome Extentions
Install the following google chrome extensions.

* [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en)
* [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en)
* [SelectorGadget](https://chrome.google.com/webstore/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb)
* [Regex Search](https://chrome.google.com/webstore/detail/regex-search/bcdabfmndggphffkchfdcekcokmbnkjl?hl=en)
* [Web Developer](https://chrome.google.com/webstore/detail/web-developer/bfbameneiokkgbdmiekhjnmfkcnldhhm?hl=en-US)
* [Json Formatter](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa)

### Install Sublime
- Install Sublime Text 3
	- If you're on a Mac and have installed [Homebrew](https://brew.sh/) (reccomended), you can install with `brew cask install sublime-text`. Otherwise you can download it from [https://www.sublimetext.com/](https://www.sublimetext.com/).
- Install the JSON plugin for sublime text.
	- Open Sublime Text
	- Open the Command Palette with <kbd>⌘</kbd>+<kbd> Shift </kbd>+<kbd> P </kbd> (use <kbd>CTRL</kbd>+<kbd> Shift </kbd>+<kbd> P </kbd> on Windows)
	- Type: "Install Package Control" and press enter
	- Open the Command Palette again
	- Type: "Package Control: Install Package" and press enter.
	- Find the package named "JSON Reindent" and press enter to install it.

### Install Command Line Tools (optional)

Open a terminal and paste these lines in to install homebrew package manager and then the `wget` and `tree` commands:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew install wget
brew install tree
```

## How websites work
[https://projects.propublica.org/graphics/images/data-institute/presentations/how-websites-work.pdf](https://projects.propublica.org/graphics/images/data-institute/presentations/how-websites-work.pdf)

## HTML, CSS, & JavaScript

Simple website example: [https://dmil.github.io/simple-website/](https://dmil.github.io/simple-website/)

Simple website code: [https://github.com/dmil/simple-website](https://github.com/dmil/simple-website)

## URLs (URIs)

Uniform Resource Locator (Uniform Resource Identifier)

[What is a URL](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL) | [Anatomy of a URL](https://doepud.co.uk/blog/anatomy-of-a-url)
![](url.png)
source: https://code.tutsplus.com/tutorials/http-the-protocol-every-web-developer-must-know-part-1--net-31177

### What a URL reveals about a web app

> Furthermore, URLs have to last. Those t-shirts and links and blogs will
not disappear simply because you decided to reorganize your server, or move to a
different operating system, or got promoted and replaced by a subordinate (or voted
out of office). They will last for years and years to come, so your URLs must last
with them.
>
>Moreover, URLs do not just exist as isolated entities (like “http://
example.org/lunch/bacon.html”). They combine to form patterns
(“bacon.html”, “lettuce.html”, “tomato.html”). And each of these
patterns finds its place in a larger path of interaction (“/”, “/lunch/”,
“/lunch/bacon.html”).
>
> Because of all this, URLs cannot be some side-effect or afterthought, as
many seem to wish. Designing URLs is the most important part of building a web
application and has to be done first. Encoded in their design are a whole series of
implicit assumptions about what your site is about, how it is structured, and how it
should be used; all important and largely-unavoidable questions.
>
> \- [Swartz (Chapter 2:: Building for Users: Designing URLs)](http://www.morganclaypool.com/doi/pdf/10.2200/S00481ED1V01Y201302WBE005)

### More about URLs

URL Encodings (when you see strange characters in a URL, consult this table):

* https://www.w3schools.com/tags/ref_urlencode.asp

Think in terms of "Resources" if you are navigating a well built site, or especially if you're hitting a REST api (which most APIs are). For example, what are the resources on this site? What assumptions if any, can you make about how their data is structured?

* Lets check out this site together: https://www.crunchbase.com/

### Try It

1. Navigate to https://beta.fec.gov/data/advanced/
2. Observe how the URLs change across the site and discuss with the person sitting next to you. Try to map out the "resources" on their site.
3. Lets discuss as a group what this says about their site and how they store their data. 
4. Together lets look at their API https://api.open.fec.gov/developers/ and how the structure of the FEC API reflects on their site, and again what this reveals about their data.

#### Bonus

5. Lets hit the FEC API, get some JSON, convert it to CSV using an online tool
6. Get an API key, submit the same request via postman

### Why this is useful

You're steps away now from writing a program that can paginate through an API and collect all the data you need. The first step is exploring the URLs, manipulating them, and figuring out where the data you want is.

Even if you're not quite at the place where you can write the code, this will help you at least know what is possible, and a request like "paginate through these urls and give me these fields" is a really small ask. Also once you've done it once, you can do it again.

## HTTP
### HTTP Verbs: GET & POST
http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade#/6/4

GET | POST
----|-----
Requests data from a specific resource. |	Submits data to be processed by a specific resource.
Data is submitted as part of the URL | Data is submitted in the request body
Less secure but faster |	More secure but slower
Can be cached by browser |	Not Cached by Browser
Length Limited by URL size |	MaxLength determined by server

Source: 

http://slides.com/dhrumilmehta/how-to-tell-a-story-with-data-tools-of-the-trade#/6/5

http://www.w3schools.com/tags/ref_httpmethods.asp

### HTTP: Headers

![](http://www.tcpipguide.com/free/diagrams/httprequest.png)

![](http://www.tcpipguide.com/free/diagrams/httpresponse.png)

[http://www.tcpipguide.com/free/t_HTTPResponseMessageFormat-3.htm](http://www.tcpipguide.com/free/t_HTTPResponseMessageFormat-3.htm)

### HTTP: Status Codes

https://www.w3schools.com/tags/ref_httpmessages.asp

https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

### HTTP: Additional References

https://code.tutsplus.com/tutorials/http-the-protocol-every-web-developer-must-know-part-1--net-31177

http://httpbin.org
https://requestb.in/

### Try It

1. Open the postman app
2. Open http://httpbin.org in chrome
3. Lets try the following examples of GET requests together. First in chrome, then in postman

	* `/` This page.
	* `/ip` Returns Origin IP.
	* `/user-agent` Returns user-agent.
	* `/get` Returns user-agent.
	* `/response-headers?key=value` Returns given response headers.

4. Lets try the following POST requests, first on the site, then via postman

	* `/post` Returns POST data
	* `/forms/post` HTML form that submits to /post

### HTTP requests from the terminal with `curl` & `wget`

Lets first create a folder on the desktop and work inside it

![](https://www.evernote.com/shard/s150/sh/fbbd67bd-2c53-4b2b-b278-adf2412af017/8b864e264b9a4936/res/7adbc382-95ea-4a22-b80d-8ae2a2f8cc45/skitch.png?resizeSmall&width=832)

Lets get the data from this page https://projects.propublica.org/represent/expenditures

#### Using `curl`
Print results of HTTP request body to the terminal

```
curl https://pp-projects-static.s3.amazonaws.com/congress/staffers/2016Q3-house-disburse-detail.csv
```

Print results of HTTP request body to the terminal and pipe output to a file

```
curl https://pp-projects-static.s3.amazonaws.com/congress/staffers/2016Q3-house-disburse-detail.csv > 2016Q3data.csv
```

Print results of three HTTP requests to the terminal (Q1, Q2, Q3) and pipe output to a file

```
curl https://goo.gl/Q3QDRb https://goo.gl/6B5xAV https://goo.gl/e6JPwS > 2016data.csv
```
alternatively

```
curl https://pp-projects-static.s3.amazonaws.com/congress/staffers/2016Q{1,2,3}-house-disburse-detail.csv > 2016data.csv
```

#### Using `wget`

Save results of HTTP request body to file

```
wget https://pp-projects-static.s3.amazonaws.com/congress/staffers/2016Q3-house-disburse-detail.csv
```

Save results of several HTTP requests to several files

```
wget https://pp-projects-static.s3.amazonaws.com/congress/staffers/20{09,10,11,12,13,14,15,16}Q{1,2,3,4}-house-disburse-detail.csv
```

### Try It

https://projects.propublica.org/represent/expenditures

1. Use `curl` to grab all the data from the "summary" files, and pipe them into a single file called `summary.csv`
2. Use `wget` to downoad all of the summary files individually

### Why this is Useful

* You can get data with curl
* If you know how to manipulate URLS, you can get data with postman
* Writing scrapers is essentially just the art of figuring out which GET and POST requests to make in which order and selecting data with CSS selectors (coming up next). Figuring out those things means you've already done most of the legwork leading up to writing a scraper.

## Hunting for Data

### The Network Tab: Finding a Hidden API
* http://data.desmoinesregister.com/iowa-caucus/candidate-tracker/index.php
* http://www.gallup.com/poll/113980/Gallup-Daily-Obama-Job-Approval.aspx

### Try It
Can you find the data?

* https://obamawhitehouse.archives.gov/interactive-budget
* http://polling.reuters.com/#poll/TR130

### Journalism from the Network Tab

http://money.cnn.com/2015/01/21/technology/security/obamacare-website-advertisers/

https://www.eff.org/deeplinks/2015/01/healthcare.gov-sends-personal-data

https://fivethirtyeight.com/features/fandango-movies-ratings/

## Additional Resources
* JavaScript for Cats [http://jsforcats.com/](http://jsforcats.com/) 
	- Learn the basics of JavaScript using the console window in your browser. Takes only about an hour!
* Adding JS snippets to your console window.
  * `console.save` command: https://coderwall.com/p/prhwzg/add-console-save-to-chrome
  * More! http://bgrins.github.io/devtools-snippets/

### Software to Know About

* [Charles Proxy (Mac)](https://www.charlesproxy.com/)
* [Yesware](http://www.yesware.com/)
* [WireShark](https://www.wireshark.org/)
* [Postman Interceptor](https://chrome.google.com/webstore/detail/postman-interceptor/aicmkgpgakddgnaphhhpliifpcfhicfo?hl=en)

