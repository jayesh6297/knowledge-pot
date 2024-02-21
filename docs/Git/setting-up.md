# Setting up git

!!! note
	we are setting up git for global config and https not for ssh

- `git --global config user.name "your_user_name"` will set the username of git
- `git --global config user.email "your_email"` will set the email
- `git config --global credential.helper store` this will cache the git credentials on your system	

!!! warning
	since the git credentials are stored in plain text it is advised used some encryption
	we are doing this to quickly setup the workspace so you can read addtional documentation
	on storing git crendetials

!!! tip
	you can also include it in any linux distribution using libsecret package needs to be installed is `libsceret` this may be named differntly for different distributions. `git config --global credential.helper /usr/lib/git-core/git-credential-libsecret` hit this command and enter your username and password for first push then it won't ask for password again. Now if you can't find same path under other distribution you can always use command `locate -b git-credential-libsecret`. optionally you can try https://github.com/hickford/git-credential-oauth this library to authenticate using oauth installation instruction are given in repo.: