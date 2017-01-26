# Skip Lmod initialization if USER_IS_ROOT or LMOD_DISABLE is set

if ( $?USER_IS_ROOT || $?LMOD_DISABLE ) then
  exit
endif

if ( ! $?__Init_Default_Modules )  then
  if ( ! $?LMOD_SYSTEM_DEFAULT_MODULES ) then
    if ( -f "/usr/share/modulefiles/DefaultModules.lua" ) then
      setenv LMOD_SYSTEM_DEFAULT_MODULES "DefaultModules"
    else
      if ( -f "/usr/share/modulefiles/StdEnv.lua" ) then
        setenv LMOD_SYSTEM_DEFAULT_MODULES "StdEnv"
      endif
    endif
  endif
  module --initial_load restore
  setenv __Init_Default_Modules 1
else
  module refresh
endif
