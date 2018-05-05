# Setup

1. Open `Terminal.app` from the Applications folder. You can press Cmd+Space to initiate Spotlight and then type `Terminal`.

	*`Terminal.app` is how we will run command line software. Instead of clicking buttons on graphical user interfaces (GUIs), we will type commands on the command line (CLI).*

1. Install [XCode](https://developer.apple.com/xcode/) Command Line Tools.

	```
	xcode-select --install
	```
	
	*This command installs a basic set of command line tools that are necessary to get started.*

2. Install the [Homebrew](https://brew.sh/) package manager.

	```
	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	```
	
	*A package manager is akin to an app store (except everything is free!). We will use homebrew and it's GUI extension, homebrew-cask to install the necessary CLI and GUI applcations.*
	
3. Install necessary packages using the following commands:

	*If you already have Sublime Text or iTerm2 installed, I recommend uninstalling (dragging to Trash) the app first and re-installing via brew cask as shown below.*

	*When you see multiple lines, copy them one by one after waiting for the previous command to finish.*

	```
	brew update
	brew upgrade
	brew cleanup
	brew install python tree wget jq pup
	brew cask install sublime-text iterm2 sourcetree
	pip3 install requests bs4 csvkit
	```

4. Verify that everything is installed correctly.

	*When you see a $ dollar sign, it signals the start of a command line prompt. It is used to differentiate between what you should type vs. what the output should look like (usually right below).*

	```
	$ which python3
	/usr/local/bin/python3
	```

	```
	$ python3 --version
	Python 3.6.5
	```

	```
	$ which csvcut 
	/usr/local/bin/csvcut
	```

	```
	$ subl .
	```

	Sublime Text 3 should open up.

	Open `iTerm.app` from the Applications directory. We will now use this program instead of `Terminal.app`.
