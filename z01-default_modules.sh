# Skip Lmod initialization if USER_IS_ROOT or LMOD_DISABLE is set

([ -n "$USER_IS_ROOT" ] || [ -n "$LMOD_DISABLE" ]) && exit

if [ -z "$__Init_Default_Modules" ]; then
  export __Init_Default_Modules=1;
  if [ -z "$LMOD_SYSTEM_DEFAULT_MODULES" ];then
    if [ -f "/usr/share/modulefiles/DefaultModules.lua" ];then
      export LMOD_SYSTEM_DEFAULT_MODULES="DefaultModules"
    else
      if [ -f "/usr/share/modulefiles/StdEnv.lua" ];then
        export LMOD_SYSTEM_DEFAULT_MODULES="StdEnv"
      fi
    fi
  fi
  module --initial_load restore
else
  module refresh
fi
