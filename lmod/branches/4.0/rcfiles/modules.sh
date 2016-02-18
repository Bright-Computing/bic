if [ `id -u` -ne 0 ]; then 
  export MODULEPATH=/cvos/local/modulefiles:/cvos/shared/modulefiles
  export PATH=${PATH}:/sbin:/usr/sbin
else 
  export MODULEPATH=/cvos/local/modulefiles
fi
