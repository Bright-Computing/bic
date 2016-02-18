if ( `id -u` != "0" ) then 
  set modulepath_tmp = /cm/local/modulefiles:/cm/shared/modulefiles
  set path_tmp = /sbin:/usr/sbin:/cm/local/apps/environment-modules/__VERSION__/bin
else
  set modulepath_tmp = /cm/local/modulefiles
  set path_tmp = /cm/local/apps/environment-modules/__VERSION__/bin
endif
if ($?MODULEPATH) then
  if ( `echo "X${MODULEPATH}Y" | grep "[X:]${modulepath_tmp}[Y:]"` != "X${MODULEPATH}Y" ) then
    setenv MODULEPATH ${MODULEPATH}:${modulepath_tmp}
  endif
else
  setenv MODULEPATH ${modulepath_tmp}
endif
if ($?PATH) then
  if ( `echo "X${PATH}Y" | grep "[X:]${path_tmp}[Y:]"` != "X${PATH}Y" ) then
    setenv PATH ${PATH}:${path_tmp}
  endif
else
  setenv PATH ${path_tmp}
endif
unset modulepath_tmp
unset path_tmp
