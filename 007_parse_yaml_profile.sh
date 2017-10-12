PARSEFILES=$(ls /etc/profile.definitions/{global,site/*,nodecategory/*,groups/`id -gn`,user/`id -un`}.yml 2>/dev/null)

if [ -z "$__Init_Default_Profile" ]; then
  export __Init_Default_Profile=1;
  if [ -z $1 ]; then
    eval `cat /dev/null $PARSEFILES | bash /etc/profile.definitions/parse_yaml.sh |sed 's/^/export /g;s/[[:space:]]*#.*//g'`
  else
    cat /dev/null $PARSEFILES | bash /etc/profile.definitions/parse_yaml.sh|sed 's/^/export /g;s/[[:space:]]*#.*//g'
  fi
fi

unset PARSEFILES
