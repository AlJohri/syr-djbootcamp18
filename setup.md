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

4. Re-initialize the shell with the changes to `.bash_profile`.

```
exec "$SHELL"
```

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
