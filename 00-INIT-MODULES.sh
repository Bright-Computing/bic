if [ -z "$MODULEPATH" ]; then

  export MODULEPATH=/etc/modulefiles:/usr/share/modulefiles:/usr/share/Modules/modulefiles:/etc/site/modules

  ## Initializations
  export LMOD_RC=/etc/site/extras/lmodrc.lua
  export LMOD_SYSTEM_DEFAULT_MODULES="use.own.eb" ## "HPCBIOS/2015q2 sge cluster"
  export LMOD_PACKAGE_PATH=/etc/site/lmod
  export LMOD_TMOD_FIND_FIRST=true
  export LMOD_ADMIN_FILE=/dev/shm/lmod/lmod_admin_file

fi
