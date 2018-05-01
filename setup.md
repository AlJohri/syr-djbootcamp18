# Setup

1. Open `Terminal.app` from the Applications folder.

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

	```
	brew update
	brew upgrade
	brew install python3 tree wget
	brew cask install sublime-text iterm2
	pip3 install csvkit
	```
