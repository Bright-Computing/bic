# -*- shell-script -*-
########################################################################
#  This is the system wide source file for setting up
#  modules:
#
########################################################################

if [ -n "${USER_IS_ROOT}" ];then
  exit
fi

# Lmod is initialized only for non-root users

if [ -z "${MODULEPATH_ROOT:-}" ]; then
  export USER=${USER-${LOGNAME}}  # make sure $USER is set
  export LMOD_sys=`uname`

  LMOD_arch=`uname -m`
  if [ "x$LMOD_sys" = xAIX ]; then
    LMOD_arch=rs6k
  fi
  export LMOD_arch

  export MODULEPATH_ROOT="/usr/share/modulefiles"
  export LMOD_SETTARG_CMD=":"
  export LMOD_FULL_SETTARG_SUPPORT=no
  export LMOD_COLORIZE=yes
  export LMOD_PREPEND_BLOCK=normal
  # export MODULEPATH=$(/usr/share/lmod/lmod/libexec/addto --append MODULEPATH $MODULEPATH_ROOT/$LMOD_sys $MODULEPATH_ROOT/Core)
  # export MODULEPATH=$(/usr/share/lmod/lmod/libexec/addto --append MODULEPATH /usr/share/lmod/lmod/modulefiles/Core)
  export MODULESHOME=/usr/share/lmod/lmod

  export BASH_ENV=$MODULESHOME/init/bash

  #
  # If MANPATH is empty, Lmod is adding a trailing ":" so that
  # the system MANPATH will be found
  if [ -z "${MANPATH:-}" ]; then
    export MANPATH=:
  fi
  export MANPATH=$(/usr/share/lmod/lmod/libexec/addto MANPATH /usr/share/lmod/lmod/share/man)
fi

PS_CMD=/usr/bin/ps
if [ ! -x $PS_CMD ]; then
    if   [ -x /bin/ps ]; then
        PS_CMD=/bin/ps
    elif [ -x /usr/bin/ps ]; then
        PS_CMD=/usr/bin/ps
    fi
fi
EXPR_CMD=/usr/bin/expr
if [ ! -x $EXPR_CMD ]; then
    if   [ -x /usr/bin/expr ]; then
        EXPR_CMD=/usr/bin/expr
    elif [ -x /bin/expr ]; then
        EXPR_CMD=/bin/expr
    fi
fi
BASENAME_CMD=/usr/bin/basename
if [ ! -x $BASENAME_CMD ]; then
    if   [ -x /bin/basename ]; then
        BASENAME_CMD=/bin/basename
    elif [ -x /usr/bin/basename ]; then
        BASENAME_CMD=/usr/bin/basename
    fi
fi


my_shell=$($PS_CMD -p $$ -ocomm=)
my_shell=$($EXPR_CMD    "$my_shell" : '-*\(.*\)')
my_shell=$($BASENAME_CMD $my_shell)
if [ -f /usr/share/lmod/lmod/init/$my_shell ]; then
   .    /usr/share/lmod/lmod/init/$my_shell >/dev/null # Module Support
else
   .    /usr/share/lmod/lmod/init/sh        >/dev/null # Module Support
fi
unset my_shell PS_CMD EXPR_CMD BASENAME_CMD
