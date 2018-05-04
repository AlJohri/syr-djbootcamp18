# Git: Introduction

Wikipedia
> Git (/ɡɪt/[8]) is a version control system (VCS) for tracking changes in computer files and coordinating work on those files among multiple people. It is primarily used for source code management in software development,[9] but it can be used to keep track of changes in any set of files. As a distributed revision control system it is aimed at speed,[10] data integrity,[11] and support for distributed, non-linear workflows.[12]

Github

> Git is an open source program for tracking changes in text files.
> https://help.github.com/articles/github-glossary/

## What is Git?

Keeping track of file versions is hard.
![](http://petapixel.com/assets/uploads/2015/07/psdrevisioning.jpg)

### So what is Git, and why does it help us?
Above all else, Git is a fast and **distributed** version control system, that allows you to efficiently handle projects large and small.

Here are some problems we face as developers, and how git solves them:

#### Reverting to past versions

Git allows us to make save points at any time. These save points are called 'commits'. Once a save point is made, it's permanent, and allows us to go back to that save point at any time. From there, we can see what the code looked like at that point, or even start building off that version.

#### Keeping track of what each version 'meant'

Every commit has a description (commit message), which allows us to describe what changes were made between the current and previous commit. This is usually a description of what features were added or what bugs were fixed.

Additionally, git supports tagging, which allows us to mark a specific commit as a specific version of our code (e.g. '2.4.5').

#### Comparing changes to past versions

It's often important to see content of the actual changes that were made. This can be useful when:

* tracking down when and how a bug was introduced
* understanding the changes a team member made so you can stay up-to-date with progress
* reviewing code as a team for correctness or quality/style

Git allows us to easily see these changes (called a `diff`) for any given commit.

#### Fearlessness in making changes

In developing software, we often want to experiment in adding a feature or
refactoring (rewriting) existing code. Because git makes it easy to go back to a
known good state, we can experiment without worrying that we'll be unable to
undo the experimental work.

## Git (and GitHub), for things other than code
* Auditing system for changes on a file
* For collaboratively editing a text document
* Open Journalism
	* https://data.fivethirtyeight.com/
	* https://www.datajournalismawards.org/project-listing/?project_id=2082
	* 	https://github.com/showcases/open-journalism
* [For drafting government web design standards!](https://github.com/18F/web-design-standards)
* Design (image diff) 
	* https://help.github.com/articles/rendering-and-diffing-images/
* Open [comment period](https://github.com/whitehouse/source-code-policy/issues?q=is%3Aissue+is%3Aclosed) for policy
* [Drafting](https://github.com/twitter/innovators-patent-agreement) and [collaborating on](https://github.com/twitter/innovators-patent-agreement/issues) legal documents
* Github for Government
	* https://government.github.com/
	* https://government.github.com/community/
* GitHub is also a very social place
	* For making friends
		* https://twitter.com/DataDhrumil/status/979039573090152448
		* Also how I met several guest speakers for my course.
	* For [finding sources](https://github.com/search?utf8=%E2%9C%93&q=onondaga&type=) ( just use the search features to find code, and code is written by people! )
	* For [communicating with readers](https://github.com/fivethirtyeight/data/issues/85) - also so that others can [check your work](https://github.com/fivethirtyeight/data/issues?q=is%3Aissue+is%3Aclosed).
	* For finding other people who have worked on a dataset and can help you understand it.
	* For falling in love? ... maybe, i'm sure it must have happened.