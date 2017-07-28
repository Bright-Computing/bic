if [ -z "$MODULEPATH" ]; then

  export MODULEPATH=/etc/modulefiles:/usr/share/modulefiles:/usr/share/Modules/modulefiles:/etc/site/modules

  ## Initializations
  export LMOD_RC=/etc/site/lmod/lmodrc.lua
  export LMOD_SYSTEM_DEFAULT_MODULES="settarg use.own.eb HPCBIOS/2016q2 sge cluster"
  export LMOD_FULL_SETTARG_SUPPORT=yes
  export LMOD_TMOD_FIND_FIRST=yes
  export LMOD_ADMIN_FILE=/dev/shm/lmod/lmod_admin_file
  export LMOD_PACKAGE_PATH=/etc/site/lmod

fi
