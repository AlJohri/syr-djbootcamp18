# Visualizing Data

## Lets talk about charts

Slides from Julia Wolfe - Visual Journalist @ FiveThirtyEight
- Part 1 https://docs.google.com/presentation/d/1-NPLxkrjyuIPwSwqELDxkxphZVyRp2KNkmKLzOgIF7s/edit#slide=id.p
- Part 2 https://docs.google.com/presentation/d/1G_oIaChf91reAJAEoaQEXrd7N5oFaAaN67jJGuQa16o/edit#slide=id.p

## Charts tell a story

- Note what makes a good "hed" and "dek" for a chart - many of these charts tell a story by themselves.
- Note the use of "heiarchy" - where do your eyes go and what does the reader take away on first glance? On closer inspection? 

Some of our daily charts from stories I've worked on:

- https://fivethirtyeight.com/features/the-art-of-cherry-picking-polls/
- https://fivethirtyeight.com/features/republicans-cant-depend-on-minority-candidates-to-win-minority-votes/
- https://fivethirtyeight.com/features/where-trump-got-his-edge/
- https://fivethirtyeight.com/features/trump-isnt-tweeting-about-the-polls-anymore/
- https://fivethirtyeight.com/features/the-media-really-has-neglected-puerto-rico/
- https://fivethirtyeight.com/features/all-the-cable-news-networks-are-covering-the-russia-story-just-not-the-same-one/
- https://fivethirtyeight.com/features/how-much-the-polls-missed-by-in-every-state/

An interesting example:

- https://fivethirtyeight.com/features/how-a-warm-winter-destroyed-85-percent-of-georgias-peaches/

Some better examples from my colleagues on the visuals team:

- https://fivethirtyeight.com/features/what-lies-in-irmas-path/
- https://fivethirtyeight.com/features/hurricane-harveys-impact-and-how-it-compares-to-other-storms/
- https://fivethirtyeight.com/features/how-americans-order-their-steak/
- https://fivethirtyeight.com/features/gun-laws-stop-at-state-lines-but-guns-dont/
- https://fivethirtyeight.com/features/every-color-of-every-lightsaber-in-star-wars-in-one-chart/
- https://fivethirtyeight.com/features/this-was-the-slowest-boston-marathon-since-the-1970s/
- https://fivethirtyeight.com/features/20-years-of-congresss-budget-procrastination-in-one-chart/

## D3 JS (Data Driven Documents)
D3 JS

* https://d3js.org/
* https://github.com/d3/d3/wiki/Gallery

Grammar of Graphics

* https://www.amazon.com/Grammar-Graphics-Statistics-Computing/dp/0387245448

What D3 is Not

* http://ruoyusun.com/2014/05/26/what-d3js-is-not.html

### D3 Chart Examples

- http://bl.ocks.org/mbostock (Mike Bostock created D3JS, these are his examples)
- http://bl.ocks.org/ (same website, examples by different people)
- https://d3js.org/
- http://christopheviau.com/d3list/gallery.html
- https://github.com/d3/d3/wiki/Gallery

### How to select a chart type

* Financial Times Visual Vocabulary
	- https://github.com/ft-interactive/chart-doctor/blob/master/visual-vocabulary/poster.png
* Financial Times "chart doctor"
	- https://www.ft.com/chart-doctor

## Getting Started

Lets grab some code from a basic D3 visualization and get it up and running on a **separate page** on your website. We'll use this bubble chart to start with: https://bl.ocks.org/AlJohri/4d684570a395ab00a94b86f27bd8ded4

### ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example - Part 1

1. Create an empty flile called `bubble.html` and one called `bubble-data.csv` and open the folder with Sublime Text in the `data-story` repo.

	```
	cd ~/Development/data-story
	touch bubble.html
	touch bubble-data.csv
	subl .
	```

2. Grab the code from the example block and put it in `bubble.html`, grab the data and put it in `bubble-data.csv`.
 https://bl.ocks.org/AlJohri/4d684570a395ab00a94b86f27bd8ded4

3. Turn on your HTTP server in the `data-story` directory.

	```
	python3 -m http.server
	```

	press CMD-D

	```
	open http://localhost:8000/bubble.html
	```

4. Once you're sure it works, lets commit and push that.

	```
	git commit -m "add an example bubble chart"
	git push
	```

## Splitting out HTML, CSS, JavaScript and Data Files

The problem with this is that the HTML is ill-formed (there is no head and body). Also the CSS and the JavaScript is all in the same file as the HTML. Messy! I will demand that you always keep them separated for this class. Lets go ahead and do that.

Remember, a good HTML document has a head and body.

```html
<!DOCTYPE html>
<html>

<head>
  <title> Example Site </title>
</head>

<body>
</body>

</html>
```

You can link a separate CSS file with the following code. Remember, linking CSS always happens in the **\<head> \</head>** of the document.

```html
<link href="style.css" rel="stylesheet" type="text/css">
```

You can call a JavaScript file like with this code. In this case we're linking one peice of code (the D3 library itself) from a website, and another peice of code (our specific chart) form a local file. Javascript is customarily placed at the end of the **\<body> \</body>** of the document. It is usually the last line before you close the body tag.

```html
<script src="//d3js.org/d3.v4.min.js"></script>
<script src="script.js"></script>
```

### ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example - Part 2

1. Split out the JavaScript into a separate file called `bubble.js`.
2. Split out the CSS into separate file called `bubble.css`.
3. Import those files into your HTML. Your `bubble.html` might look something like this now.

	```html
	<!DOCTYPE html>
	<html>

	<head>
	  <title> Example Site </title>
	  <!--Load StyleSheets in the head-->
	  <link href="bubble.css" rel="stylesheet" type="text/css">
	</head>

	<body>
		<h1> my bubble chart </h1>

		<p> bubble bubble bubble </p>

		<!-- Run JavaScript scripts in the body -->
		<script src="//d3js.org/d3.v4.min.js"></script>
		<script src="bubble.js"></script>
	</body>

	</html>
	```
	
## Avoiding Conflicting CSS

Right now the chart works fine, however, that is because the chart is the only thing on the page. The CSS in these example D3 examples often assume the D3 is the only thing on the page. So if there were other things on the page, the CSS might also end up applying to those things as well! To avoid that, we must specify that the CSS only apply to the chart. Lets modify the CSS selectors to do just that.

### Using `id` and `class` tags Properly

But what if we want to have two charts on the page? And they're both SVGs! In that case each chart would need a unique `id` attribute. To do this we'll need to modify the d3 block.

Fortunately that is a simple change. Lets read some D3 code and see if you can figure it out.

```javascript
var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
```

Notice how that code is adding a width and a height attribute? We can add an id attribute in the same way.

```javascript
var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("class", "chart bubble-chart")
    .attr("id", "dummy-bubble-chart")
    .attr("height", height + margin.top + margin.bottom)
```

Now it will generate the chart with `id=dummy-bubble-chart` and `class=chart bubble-chart`. This allows us to:

1. Modify the CSS so that it applies only to this one chart using an id-selector (`#dummy-bubble-chart`)

2. Modify some CSS so that it applies to all bubble charts using a class-selector (`.bubble-chart`)

3. Modify some CSS so that it applies to all charts using a class-selector (`.chart`)

This is useful for standardizing styles across the site and giving everything a common look and feel with specific customization for a chart where needed.

## Working with divs

Notice that d3 appends the visualization (support vector graphic) SVG to the body element, but we want to insert it into a specific part of the page. To do that, we use a `div` element.

We now change the following line of code from:

```javascript
var svg = d3.select("body").append("svg")
```

to:

```javascript
var svg = d3.select("#dummy-bubble-chart-container").append("svg")
```

where `#dummy-bubble-chart-container` refers to a div that we must insert into the HTML.

```
<div id="dummy-bubble-chart-container"></div>
```

## Lets move the chart into story

Now we're going to delete `bubble.html` and move the D3 visualization into your `index.html` file along with the rest of your story.

1. Create a `div` that will host the chart in the middle of the "lorem ipsum" text with an id of `#dummy-bubble-chart-container`.
2. Add a line to the bottom of the `head` tag to load `bubble.css`. Remember! CSS is ultimately compiled into one big file, so make sure that the css selectors for the chart match **only** that chart.
4. Add the lines to the bottom of the `body` tag to load the javascript:

	```html
	<script src="//d3js.org/d3.v4.min.js"></script>
	<script src="bubble.js"></script>
	```

5. Delete `bubble.html`.

## Note

Some of these pre-created D3 visualizations take in CSV format (like the simple example that we did above). Others take in a JSON format. Once you learn how to use both formats effectively, you can use:

  1. any D3 visualization that takes input as CSV or JSON (most of them)
  2. any data source that outputs data as CSV or JSON (including APIs which often serve JSON files)

If you find that you want to use a data visualization, but are not sure how to connect the dataset to the visualization, slack me, I'm happy to help you learn how to connect any particular visualization to any particular dataset (JSON or CSV).

## Organizing your Code

[https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Dealing_with_files](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Dealing_with_files)
