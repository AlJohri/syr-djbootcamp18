# Git: Reference

# Getting Started

1. Create a new repository on GitHub
2. **Clone** that repository locally onto your computer

	```
	git clone git@github.com:dmil/mehta-simple-website.git
	```

# Linear Workflow


1. `cd` into the folder containing your project.

	```
	cd ~/path/to/project
	```
2. Check the **status** of your **local repository** to make sure you didn't forget to commit any work.

	```
	git status
	```

3. Then **pull** the latest changes from the **remote repository** on GitHub.

	```
	git pull
	```

4. Do a discrete chunk of work on your project (lets say you added a basic FAQ page"

5. Check the status again, then **add** the files you'd like to commit to the **staging area**.

	```
	git status
	git add faq.html
	git status
	```
6. Commit with a descriptive summary of exactly what you did

	```
	git commit -m "add a basic FAQ page"
	```

7. Push that change back to GitHub

	```
	git push
	```

# Non-Linear Workflow

We won't discuss the exact workflow here, but the non-linear workflow involves maintaining a "master branch", which is the main version of your project. Each feature is then developed in a "feature branch". Many people can have many different feature branches going on a project at the same time. 

As work is completed, feature branches are merged into the master branch and any conflicts (for example if I make the background of our website blue in my branch but another team member makes it green in their branch) are resolved.