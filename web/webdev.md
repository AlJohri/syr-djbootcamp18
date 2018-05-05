# Web Dev Basics

Today we're going to learn the basics of web development. Although you may not need to know how to develop websites from scratch these days to get content on the web (you can use squarespace, wordpress, medium, etc.), knowing how these tools work will:

- help you better understand the web as a medium for publishing
- help you learn how website are built in order to be able to extract data from them
- give you a starting point if you're interested in learning how to build custom data visualizations or take on any additional technical learning involving the web

We'll be leaning on Mozilla's tutorials (with some tweaks) to learn the basics of HTML, CSS, and JavaScript. Once we're all on the same page, we will modify the website the tutorial has us build into a template for a data-driven story. 

Your objective after this technical bootcamp is over will be to add content to that template and tell a narrative story using your newfound web development skills.

## HTML

* Tutorial: https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics

## CSS
* Tutorial: https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics

### Addendum: Attributes - Class vs ID

The `class` and `id` attributes are particularly important. These are what the CSS is going to latch onto in order to identify which elements should receive the same styles, and they are what the JavaScript will latch onto in order to determine which element it should assign a behavior to.

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Example

1. Lets put all the main content of the page within an `article` tag.

	```html
	<!DOCTYPE html>
	<html>
	<head>
	    <title></title>
	</head>
	<body>

		<article>
			<p>Lorem Ipsum....</p>
			<!-- all the rest of the content -->
		</article>

	</body>
	</html>

	```

2. Lets add a `header` with a byline and date at the top of the `article` tag.

	```html
	<article>

		<header>
			<h1 class="headline">My Awesome Article</h1>
			<div class="byline">
			    <address class="author">By <a rel="author" href="https://twitter.com/AlJohri">Al Johri</a></address> 
			    on <time pubdate datetime="2018-05-05" title="May 5th, 2018">5/5/2018</time>
			</div>
		</header>

		<!-- all the content -->

	</article>
	```

3. Lets try this by adding a few more paragraphs of text. You can generate dummy text at https://www.lipsum.com/. 5 paragraphs should be enough.

4. Lets put each one of the paragraphs in a pararaph tag.

5. Between the paragraphs of lorem ipsum, lets add some more paragraph tags, but lets make these what we'd call a pullquote. Notice that the paragraphs that are quotes have an attribute `class=quote` and the first one has an attribute `id=mainquote`.

	
	```html
	<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras semper tellus quis est lacinia, non consectetur urna consequat. Aliquam sed finibus ipsum. Suspendisse nec euismod nibh. Donec id orci risus. Aliquam erat volutpat. Praesent in sem diam. Nam rutrum dui vitae ante scelerisque gravida. In eget erat sed tellus dignissim tincidunt eget non eros. Nulla facilisi. Aenean arcu tellus, gravida sed ex ut, pellentesque dapibus erat. Duis quis quam eget diam rhoncus euismod. </p>
	
	<p id="mainquote" class="quote"> "Web development is cool" - Bill Joe Smith </p>
	
	<p> Vestibulum vel sodales augue, quis rhoncus augue. Mauris id ligula turpis. Nulla facilisis massa sed pretium ornare. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nunc nunc elit, euismod quis enim sed, hendrerit posuere dui. Aenean tempus lacinia turpis non molestie. Nullam imperdiet nibh erat, non aliquet nulla congue ac. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec feugiat enim vitae tempus euismod. Curabitur cursus eget orci vitae interdum. Sed varius luctus massa sit amet rhoncus. Morbi eget massa quis nibh tempor varius sit amet non felis. </p>
	
	<p class="quote"> "Web development is cool" - Bill Joe Smith </p>
	
	<p> In eget nisi pulvinar, dapibus enim vel, molestie eros. Donec facilisis odio sed massa pharetra cursus. Nullam felis ipsum, semper vitae hendrerit in, iaculis id enim. Mauris non consequat augue. Donec a placerat sem. Aenean lacus nibh, ullamcorper eu lacus quis, facilisis pretium quam. Donec pellentesque, metus at auctor dignissim, ligula purus tincidunt mi, sit amet eleifend tellus nulla vitae orci. Donec eget ipsum sem. In laoreet ac risus quis tristique. Suspendisse felis odio, cursus id sapien non, tincidunt euismod enim. Praesent in nisi justo. Mauris in bibendum elit. In hac habitasse platea dictumst. </p>
	
	<p> Sed quis egestas nunc. Donec dignissim scelerisque posuere. Maecenas eu ipsum justo. Fusce id dui lectus. Nulla aliquet pharetra aliquam. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam eu tincidunt quam, lacinia imperdiet massa. Duis sed vestibulum odio. </p>
	
	<p class="quote"> "JavaScript is the language of web browsers" - John Doe </p>
	
	<p> Sed scelerisque commodo odio, ut consectetur arcu sodales in. Curabitur vitae rhoncus arcu. Mauris hendrerit rhoncus diam sit amet hendrerit. Suspendisse potenti. Aenean semper rhoncus mi, non semper urna porta nec. Quisque condimentum est et ultricies aliquam. Etiam et eros in dolor tempus maximus eu id turpis. Aliquam ac leo sed ligula tincidunt vulputate. Suspendisse sagittis et mauris in euismod. Integer suscipit sapien sit amet nunc finibus, sed faucibus dui dictum. Phasellus ac velit nisi. </p>
	```

4. Make all the quotes red. Commit and push the change.
5. Make the mainquote retain all of the styles from the regular quote, but also give it a border.

## JavaScript

* Tutorial: [https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics) (do Hello World only)

* Introducing Alerts

	```javascript
	alert('Warning, this is a popup alert!!!');
	```
	
	running that in the console window will make a JavaScript alert pop up.

* Introducing Events

	We don't want that to happen as soon as you load the page though, so lets assign it an event. Lets make the image pop open an alert when you click on the fox.

	
	```javascript
	// Define a Function
	function sayOuch() {
		alert('Ouch! Stop poking me!');
	}
	
	// Use a CSS selector to identify an element
	var foxImage = document.querySelector('img');
	
	// Assign the function to the onclick event on that element
	foxImage.onclick = sayOuch;
	```
	
### Bonus
Add two buttons to your page, one to show the fox and one to hide it.

### Super duper bonus
Make those into one button that toggles show/hide of the fox

## A note about style

There are lots of tools online to help you select a color pallate:

* https://color.adobe.com/
* https://www.google.com/search?q=css+color+palette&spell=1&sa=X&ved=0ahUKEwiWg_fZ28bYAhXHzIMKHVDICKoQvwUIJigA&biw=834&bih=639
* https://www.w3schools.com/colors/colors_picker.asp

Also, you can modify CSS in the browser window if you just want to see what a change might look like without actually making the change.
