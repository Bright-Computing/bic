if ( $?USER_IS_ROOT ) then
  exit
endif

# Lmod is initialized only for non-root users

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
