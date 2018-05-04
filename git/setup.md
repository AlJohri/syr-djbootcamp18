# Git: Setup

1. Configure `git` with your name and email address. Be sure to use the same email associated with your Github account.

	```
	git config --global user.name "YOUR NAME"
	git config --global user.email "YOUR EMAIL ADDRESS"
	```

2. First lets see if you already have SSH keys setup

Follow these instructions for connecting to Github via SSH.

https://help.github.com/articles/connecting-to-github-with-ssh/

## Lets see what we've just done

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

## What can you do with these?

* Securely communicate with GitHub.
* Use them to encrypt files, data, or messages.
	* https://gist.github.com/colinstein/de1755d2d7fbe27a0f1e
* Securely leak sensitive information to journalists
	* https://securedrop.org/
	* https://www.propublica.org/article/how-to-leak-to-propublica
* Use secure shell (`ssh`) to remote into another computer.
	* `ssh fivethirtyeight@538stats` 
	*  and also show it on VNC (remote login)
* Copy a file securely from another computer using secure  copy (`scp`).
* Encryption also is at the core of cryptocurrencies. To transfer a cryptocurrency.
	* https://walletgenerator.net/
* Verifying Identity, Chat, etc... (see keybase)
* Encrpytion systems involving public and private keys (asymmetric encrpytion) are also used in apps for secure communication like WhatsApp or Signal.

## So this is what encryption is all about?

Yeah, its a really powerful tool that doesn't require a geeky genius to use. You can get started at https://keybase.io
