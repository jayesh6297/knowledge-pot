# Setting up git

## setting up with https
---
- set user name `git config --global user.name "your_user_name"`
- set email `git config --global user.email "your_email"`
- install library `libsecret` the library name may change depdending upon linux distribution
- this will save credentials to gnome-keyring or libsecret `git config --global credential.helper /usr/lib/git-core/git-credential-libsecret`
- if you can't find this path `/usr/lib/git-core/git-credential-libsecret` then you can use `locate -b git-credential-libsecret`
- credentials store with libsecret are encrypted so they are secure

!!! tip "optional"
	you can try https://github.com/hickford/git-credential-oauth this library to authenticate using oauth installation instruction are given in repo.

## setting up with ssh
---
- install `openssh` package in your system
- enable service to start on startup for ssh daemon and keygen using `sudo systemctl enable --now sshd sshdgenkeys`
- run this command to generate keys `ssh-keygen -t ed25519 -C "your_name-git"`
- provide filename to save generally i recommend to use githubusername-git
- there will be 2 files generated in current directory one public key .pub extension and other without extension that's your private key
- finally add the ssh key to ssh-agent using `ssh-add path-to-files/you_name-git` remember always add private key
- if ssh-agent is not started you can start it by using ``` eval \`ssh-agent\` ```and then again follow previous step.
- now go to github settings &rarr; SSH and GPG Keys &rarr; click on New SSH Key -> put in title, and content of generated key with extension .pub
- done
