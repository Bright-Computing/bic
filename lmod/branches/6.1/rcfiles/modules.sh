if [ `id -u` -ne 0 ]; then 
  export MODULEPATH=/cm/local/modulefiles:/cm/shared/modulefiles
  export PATH=${PATH}:/sbin:/usr/sbin:/cm/local/apps/environment-modules/__VERSION__/bin
else 
  export MODULEPATH=/cm/local/modulefiles
  export PATH=${PATH}:/cm/local/apps/environment-modules/__VERSION__/bin
fi
