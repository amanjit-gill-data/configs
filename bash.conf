#!/usr/bin/bash

### BASH CONFIGS ADDED BY AMANJIT 
# source this in ~/.bashrc

# enable git completion
source ~/.git_extras/git-completion.bash

# custom prompt with git status
source ~/.git_extras/git-prompt.sh
export PS1='\[\033[00;32m\]\u@\h\[\033[00m\]:\[\033[38;5;033m\]\w\[\e[38;5;166m\]$(__git_ps1)\[\033[00m\]\$ '
export GIT_PS1_SHOWDIRTYSTATE=1
export GIT_PS1_SHOWUNTRACKEDFILES=1

# add my downloaded apps to path
# I symlink them all under /opt/bin, so this is the only dir that needs to be added
export PATH="$PATH:/opt/bin"

# run pluggie from anywhere in file system
alias pluggie="~/projects/nvim-pluggie/pluggie.sh"

# navigate to config dirs
alias nvc="cd ~/.config/nvim"
alias confs="cd ~/.config/my-configs"

# prevent pycache creation
export PYTHONDONTWRITEBYTECODE=1

# change `ls` colours for directories, symlinks and executables
export LS_COLORS=$LS_COLORS:"di=01;38;5;25:ln=01;38;5;45:ex=01;38;5;35"

# set $JAVA_HOME; could also set for all users, in /etc/bash.bashrc
# note: this is the root of the java installation, not the path to the executable
export JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"

# enable autocomplete for pipx
eval "$(register-python-argcomplete3 pipx)"

