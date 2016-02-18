if [ `id -u` -ne 0 ]; then 
  MODULEPATH_TMP=/cm/local/modulefiles:/cm/shared/modulefiles
  PATH_TMP=/sbin:/usr/sbin:/cm/local/apps/environment-modules/__VERSION__/bin
else 
  MODULEPATH_TMP=/cm/local/modulefiles
  PATH_TMP=/cm/local/apps/environment-modules/__VERSION__/bin
fi
if [ -z "${MODULEPATH}" ]; then
  MODULEPATH=${MODULEPATH_TMP}
  export MODULEPATH
else
  if ! echo "X${MODULEPATH}Y" | grep -q "[X:]${MODULEPATH_TMP}[Y:]"; then 
    MODULEPATH=${MODULEPATH}:${MODULEPATH_TMP}
    export MODULEPATH
  fi 
fi
if [ -z "${PATH}" ]; then
  PATH=${PATH_TMP}
  export PATH
else
  if ! echo "X${PATH}Y" | grep -q "[X:]${PATH_TMP}[Y:]"; then 
    PATH=${PATH}:${PATH_TMP}
    export PATH
  fi 
fi
unset MODULEPATH_TMP
unset PATH_TMP
