# Git: Setup

1. Configure `git` with your name and email address. Be sure to use the same email associated with your Github account.

	```
	git config --global user.name "YOUR NAME"
	git config --global user.email "YOUR EMAIL ADDRESS"
	```

2. First lets see if you already have SSH keys setup

Follow these instructions for connecting to Github via SSH.

https://help.github.com/articles/connecting-to-github-with-ssh/

#### Lets see what we've just done

```
ls -al ~/.ssh/
```

This is your **public key**

```
cat ~/.ssh/id_rsa.pub
```

This is your **private key**

```
cat ~/.ssh/id_rsa
```
