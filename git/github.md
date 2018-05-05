# GitHub

Now that we've pushed our code to GitHub, lets explore the features that it adds.

1. Collaboration. This is HUGE! Github has a lot of great features to help you collaborate with your team.
2. Open Source. This is ALSO HUGE! Strangers can see your code and participate with you on your project. They can suggest fixes, point out errors, and start discussions. You can find other people's work, and make sure you're not duplicating something that already exists. Or you can interact with someone who has already worked on something similar to what you're trying to tackle.
3. Web Hosting! The GithubPages feature allows you to host a static website for free, right on GitHub.
4. A better visual interface. In the last lesson you learned how to merge branches locally. In this lesson we'll learn how to do the same on GitHub. Many of the functions you can perform locally are nicer to perform on GitHub's great web interface.

## Lets Dive In!

Remember, there are now two copies of your repository, your **local repository** which sits on your computer, and your **remote repository** which is on GitHub. Lets take a look a the remote repository that is on GitHub.

* https://github.com/dmil/my-simple-website

## (Some of) GitHub's Features

### The `README.md` file

Github looks for a "readme" file and renders it as you're navigating through the file structure. This is a great way to guide people through your code.

![](images/screenshot_25.jpg)

Its particularly evident on our data repository, where the overall repository has a readme, but each folder also contains its own readme.

* https://github.com/fivethirtyeight/data

Readme files are often given the `.md` extension, meaning they're written in a language called markdown that allows for nicer formatting. You can check out this [markdown cheet sheet](https://beegit.com/markdown-cheat-sheet) if you want to see how formatting works, but you can also save a readme files as plain text. Github will also detect `.txt` files, or you can just write plain text inside your `.md` file.

## Commit log

Commit Log

* https://github.com/dmil/my-simple-website/commits/master

## History, Raw, and Blame for any file

* File
	* https://github.com/fivethirtyeight/chartbuilder-2/blob/master/src/styles/core.scss
	* ![](images/screenshot_26.jpg)
* History
	* https://github.com/fivethirtyeight/chartbuilder-2/commits/master/src/styles/core.scss
* Blame
	* https://github.com/fivethirtyeight/chartbuilder-2/blame/master/src/styles/core.scss

## Editing files inside GitHub
![](images/screenshot_27.jpg)

## Drag and Drop
![](images/dragdrop.gif)

## Collaboration

Add `dmil` (that's me!) as a collaborator. Now I can push to your repository. Collaborators can push to the repository without asking your permission, they have full read and write access.

![](images/screenshot_23.jpg)

If I wasn't a collaborator, I could still work with you on an open source project through a process called forking where I can make a copy of your repository in my GitHub account, make changes, and request that you merge them back into your project. We will discuss forking more in depth later.

## Serving up Websites!

GitHub is also great for serving up static websites. Right now, you have the code for your website on GitHub, but its not being served up anywhere. GitHub is only storing the code. Luckily, if your code happens to be a website, GitHub can also host it for you through a feature called "GitHub Pages". 

Simply go to the "settings" menu, scroll down to "GitHub Pages", and select "master branch"

![](images/screenshot_24.jpg)

Whatever is in your master branch on GitHub should now appear at 

```
http://your-username.github.io/repository-name
```

in my case it is [**http://dmil.github.io/my-simple-website**](http://dmil.github.io/my-simple-website)

## Pull Requests

In the previous tutorial we merged branches locally on our computer. This is, however, not ideal when working on projects with other people. The best practice is to issue pull requests on GitHub. 

A **pull request** is a request to merge one branch into another branch. Right now our repository only has one branch, so we cannot issue a pull request.

* https://github.com/dmil/my-simple-website/branches

Lets demonstrate how branches are merged by creating a new branch
