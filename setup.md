# Setup

1. Open `Terminal.app` from the Applications folder.

1. Install [XCode](https://developer.apple.com/xcode/) Command Line Tools.

	```
	xcode-select --install
	```

2. Install the [Homebrew](https://brew.sh/) package manager.

	```
	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	```

3. Add `/usr/local/bin/` to your `$PATH`.

	```
	echo '\nexport PATH=/usr/local/bin:$PATH' >> ~/.bash_profile
	```

	*When you run the `Terminal.app`, the default prompt that is running is a program called `bash`. When `bash` starts up, it uses the `~/.bash_profile` script to initialize the environment.*

	*When you type any command, `bash` searches a list of folders to see if it can find that command. This list of folders is stored in the $PATH.*

	*The command above prepends the homebrew directory to $PATH. When we install packages through homebrew, we will now be able to directly access them by just typing in the name of the command.*

	*If this doesn't make sense, we'll review it again in class.*

4. Re-initialize the shell with the changes to `.bash_profile`.

	```
	exec "$SHELL"
	```

	*This command is re-initializing the environment (i.e. re-running the modified `.bash_profile` script).*

4. In the terminal run the following command to update your package manager.

	```
	brew update
	```

5. Install necessary packages using the following commands:

	```
	brew install python3 tree wget
	brew cask install sublime-text
	pip3 install csvkit
	```
