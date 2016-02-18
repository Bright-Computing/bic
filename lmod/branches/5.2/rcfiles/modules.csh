if ( `id -u` != "0" ) then 
  setenv MODULEPATH /cm/local/modulefiles:/cm/shared/modulefiles
  setenv PATH ${PATH}:/sbin:/usr/sbin
else
  setenv MODULEPATH /cm/local/modulefiles
endif

