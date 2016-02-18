if ( `id -u` != "0" ) then 
  setenv MODULEPATH /cvos/local/modulefiles:/cvos/shared/modulefiles
else
  setenv MODULEPATH /cvos/local/modulefiles
endif

