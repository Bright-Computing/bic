if ( ! $?__Init_Default_Modules || ! $?LD_LIBRARY_PATH )  then
  if ( ! $?LMOD_SYSTEM_DEFAULT_MODULES ) then
    if ( -f "/usr/share/modulefiles/DefaultModules.lua" ) then
      setenv LMOD_SYSTEM_DEFAULT_MODULES "DefaultModules"
    else
      setenv LMOD_SYSTEM_DEFAULT_MODULES "StdEnv"
    endif
  endif
  module --initial_load restore
  setenv __Init_Default_Modules 1
else
  module refresh
endif
