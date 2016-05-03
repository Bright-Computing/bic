if ( ! $?__Init_Default_Modules || ! $?LD_LIBRARY_PATH )  then
  if ( -f "/usr/share/modulefiles/DefaultModules.lua" ) then
    if ( ! $?LMOD_SYSTEM_DEFAULT_MODULES ) then
      setenv LMOD_SYSTEM_DEFAULT_MODULES "DefaultModules"
    endif
  endif
  module --initial_load restore
  setenv __Init_Default_Modules 1
else
  module refresh
endif
