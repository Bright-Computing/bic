if ( ! $?__Init_Default_Profile )  then
  eval "`bash /etc/profile.d/007_sh-in-it.sh OK`"
  setenv __Init_Default_Profile 1
endif
