if (! $?MODULEPATH) then

  setenv MODULEPATH /etc/modulefiles:/usr/share/modulefiles:/usr/share/Modules/modulefiles:/etc/site/modules
  
  ## Initializations
  setenv LMOD_RC /etc/site/lmod/lmodrc.lua
  setenv LMOD_SYSTEM_DEFAULT_MODULES "settarg use.own.eb" ## "HPCBIOS/2015q2 sge cluster"
  setenv LMOD_PACKAGE_PATH           /etc/site/lmod
  setenv LMOD_TMOD_FIND_FIRST        true
  setenv LMOD_ADMIN_FILE             /dev/shm/lmod/lmod_admin_file

endif
