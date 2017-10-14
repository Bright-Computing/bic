PARSEFILES=$(ls /etc/profile.definitions/{global*,site/*,nodecategory/*,groups/`id -gn`,user/`id -un`}.yml 2>/dev/null)

if [ -z "$__Init_Default_Profile" ]; then
  eval `for i in $PARSEFILES; do python /etc/profile.d/007-sh-in-it.xyzzy.py $i;done`
  export __Init_Default_Profile=1;
fi

unset PARSEFILES
