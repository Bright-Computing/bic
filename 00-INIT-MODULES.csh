if (! $?MODULEPATH) then

  setenv MODULEPATH /etc/modulefiles:/usr/share/modulefiles:/usr/share/Modules/modulefiles:/etc/site/modules
  
  ## Initializations
  setenv LMOD_RC /etc/site/extras/lmodrc.lua
  ##setenv LMOD_SYSTEM_NAME AVX2
  ##setenv LMOD_SYSTEM_DEFAULT_MODULES "HPCBIOS/2015q2 sge"
  setenv LMOD_SYSTEM_DEFAULT_MODULES "sge cluster"
  setenv LMOD_PACKAGE_PATH           /etc/site/lmod
  setenv LMOD_TMOD_FIND_FIRST        true

endif
