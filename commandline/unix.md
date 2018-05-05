## Unix

Unix (/ˈjuː.nɪks/; trademarked as UNIX) is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix, developed starting in the 1970s at the Bell Labs research center - [https://en.wikipedia.org/wiki/Unix](https://en.wikipedia.org/wiki/Unix)

Many Unix-like operating systems have arisen over the years, of which Linux is the most popular, having displaced SUS-certified Unix on many server platforms since its inception in the early 1990s. - [https://en.wikipedia.org/wiki/Unix](https://en.wikipedia.org/wiki/Unix)

* [https://en.wikipedia.org/wiki/Unix](https://en.wikipedia.org/wiki/Unix)
* [https://en.wikipedia.org/wiki/Unix_philosophy](https://en.wikipedia.org/wiki/Unix_philosophy)
* [https://en.wikipedia.org/wiki/History_of_Unix](https://en.wikipedia.org/wiki/History_of_Unix)
* [http://www.howtogeek.com/182649/htg-explains-what-is-unix/](http://www.howtogeek.com/182649/htg-explains-what-is-unix/)

## Operating System Concepts

* Files and Processes
	- Everything in UNIX is either a file or a process
	- `ps aux` to see the processes that are running, same as opening the "activity monitor"
	- [http://www.ee.surrey.ac.uk/Teaching/Unix/unixintro.html](http://www.ee.surrey.ac.uk/Teaching/Unix/unixintro.html)

* Exploring the root directory (in case you're ever wondering what all those files in `/` are)
	* [https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
	* [http://www.thegeekstuff.com/2010/09/linux-file-system-structure/?utm_source=tuicool](http://www.thegeekstuff.com/2010/09/linux-file-system-structure/?utm_source=tuicool)

## Stdin & Stdout (& Stderr)
Originally I/O happened via a physically connected system console (input via keyboard, output via monitor), but standard streams abstract this. When a command is executed via an interactive shell, the streams are typically connected to the text terminal on which the shell is running, but can be changed with redirection, e.g. via a pipeline. - [https://en.wikipedia.org/wiki/Standard_streams](https://en.wikipedia.org/wiki/Standard_streams)

![](http://www.informit.com/content/images/chap5_9780133927313/elementLinks/05fig02.jpg)

source: [http://www.informit.com/articles/article.aspx?p=2273593&seqNum=5](http://www.informit.com/articles/article.aspx?p=2273593&seqNum=5)

![](http://www.informit.com/content/images/chap5_9780133927313/elementLinks/05fig03.jpg)

Figure 5-3 By default, standard input comes from the keyboard, and standard output goes to the screen

source: [http://www.informit.com/articles/article.aspx?p=2273593&seqNum=5](http://www.informit.com/articles/article.aspx?p=2273593&seqNum=5)

### Redirection
![](http://www.informit.com/content/images/chap5_9780133927313/elementLinks/05fig04.jpg)

Figure 5-4 Redirecting standard output

`command [arguments] > filename`

source: [http://www.informit.com/articles/article.aspx?p=2273593&seqNum=5](http://www.informit.com/articles/article.aspx?p=2273593&seqNum=5)

### Piping

![](https://www.evernote.com/shard/s150/sh/85196657-a9d4-4ae5-a212-225d6c51c14c/9afdbbe4f4da9789/res/57476e92-9833-4887-9e95-3f2644475598/skitch.png?resizeSmall&width=832)

source: [https://en.wikipedia.org/wiki/Pipeline_(Unix)](https://en.wikipedia.org/wiki/Pipeline_(Unix))

## Exit Codes

Commands return exit codes when they finish running, `0`is success, `1` is fail

Get exit code of the command you just ran with the following

```
echo $?
```

Error Codes other than 1 and 0 are more rare, but here are some examples: [http://www.tldp.org/LDP/abs/html/exitcodes.html](http://www.tldp.org/LDP/abs/html/exitcodes.html])

Additional resource on exit codes:

[http://bencane.com/2014/09/02/understanding-exit-codes-and-how-to-use-them-in-bash-scripts/](http://bencane.com/2014/09/02/understanding-exit-codes-and-how-to-use-them-in-bash-scripts/)


## Permissions and `chmod`

#### Observing a file's permissions

```
ls -l
```

![](https://www.evernote.com/shard/s150/sh/e3167d0f-bb17-48dc-915f-c8fb3bc06e6d/769f5c1706fe6b35/res/2bd19ca1-fada-4833-8932-3835dfaee51c/skitch.png?resizeSmall&width=832)

![](http://linuxcommand.org/images/permissions_diagram.gif)

source: [http://linuxcommand.org/lts0070.php](http://linuxcommand.org/lts0070.php)

1. Look at permissions inside `~/Development/universe/solar_system/planets`
2. Look at permissions inside `/Applications` - notice how those are executable while the planets files are not.

#### Changing a file's permissions

`chmod` stands for "change mode", it is the command that lets you set permissions for a file

- http://computerplumber.com/2009/01/using-the-chmod-command-effectively/
- https://en.wikipedia.org/wiki/Chmod
- https://www.cise.ufl.edu/~shray/

#### sudo (super user do)

Prepend any command with `sudo` in order to run the command as root user. Try to avoid this unless you know what you're doing. But also know that it is often the solution if you get an error telling you that you don't have the permissions to run something.

[http://unix.stackexchange.com/questions/3063/how-do-i-run-a-command-as-the-system-administrator-root](http://unix.stackexchange.com/questions/3063/how-do-i-run-a-command-as-the-system-administrator-root)

![](https://imgs.xkcd.com/comics/sandwich.png)

## Nothing is Magic

Part of technical reasoning is understanding that nothing is magic. Knowing how the command line works helps you understand your computer better, and knowing the structure of websites (which we will learn later in this course) will help you better navigate web technologies. 

If something is not working, there is always a reason. Try to reason your way through the solution using google, stackoverflow, and other people as your guideposts. 

Solving coding quetions is often like feeling around in the dark with the lights off. Use context clues to guide you to the place you want to go, and if you're totally lost just shout out to someone who can shine a light in the right place.