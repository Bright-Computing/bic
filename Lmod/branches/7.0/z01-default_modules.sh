if [ -z "$__Init_Default_Modules" -o -z "$LD_LIBRARY_PATH" ]; then
   export __Init_Default_Modules=1;
   if [ -f "/usr/share/modulefiles/DefaultModules.lua" ];then
     if [ -z "$LMOD_SYSTEM_DEFAULT_MODULES" ];then
       export LMOD_SYSTEM_DEFAULT_MODULES="DefaultModules"
     fi
     module --initial_load restore
   fi
else
   module refresh
fi
