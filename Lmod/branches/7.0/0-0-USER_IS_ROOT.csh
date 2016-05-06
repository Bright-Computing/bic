#!/usr/bin/csh

set _id_=`id -u`

if ( "$_id_" == 0 ) then
  if ( ! $?USER_IS_ROOT ) then
    setenv USER_IS_ROOT 1
  endif
endif

unset _id_
