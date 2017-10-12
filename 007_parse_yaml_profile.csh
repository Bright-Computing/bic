if ( ! $?__Init_Default_Profile )  then
  eval "`bash /etc/profile.d/007_parse_yaml_profile.sh OK|sed 's/^export /setenv /g;s/=\(.*\)/ \1/g'|tr '\n' ';'`"
  setenv __Init_Default_Profile 1
endif
