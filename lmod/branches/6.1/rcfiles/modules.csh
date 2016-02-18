if ( `id -u` != "0" ) then 
  setenv MODULEPATH /cm/local/modulefiles:/cm/shared/modulefiles
  setenv PATH ${PATH}:/sbin:/usr/sbin:/cm/local/apps/environment-modules/__VERSION__/bin
else
  setenv MODULEPATH /cm/local/modulefiles
  setenv PATH ${PATH}:/cm/local/apps/environment-modules/__VERSION__/bin
endif

