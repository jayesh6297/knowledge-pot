# Setting up git

!!! note
	we are setting up git for global config

- `git --global config user.name "your_user_name"` will set the username of git
- `git --global config user.email "your_email"` will set the email
- `git config --global credential.helper store` this will cache the git credentials on your system	

!!! warning
	since the git credentials are stored in plain text it is advised used some encryption
	we are doing this to quickly setup the workspace so you can read addtional documentation
	on storing git crendetials

you can also include it in any linux distribution using libsecret. <br>
so i'm on arch right now  and package needs to be installed is `libsceret` <br>
`git config --global credential.helper /usr/lib/git-core/git-credential-libsecret` hit this command and enter your username and password for first push then it won't ask for password again<br>
now if you can't find same path under other distribution you can always use command `locate -b git-credential-libsecret`

