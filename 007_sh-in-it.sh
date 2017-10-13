PARSEFILES=$(ls /etc/profile.definitions/{global,site/*,nodecategory/*,groups/`id -gn`,user/`id -un`}.yml 2>/dev/null)

if [ -z "$__Init_Default_Profile" ]; then
  export __Init_Default_Profile=1;
  if [ -z $1 ]; then
    eval `for i in $PARSEFILES; do python /etc/profile.d/007_sh-in-it.py     $i;done`
  else
          for i in $PARSEFILES; do python /etc/profile.d/007_sh-in-it.py.csh $i;done
  fi
fi

unset PARSEFILES
