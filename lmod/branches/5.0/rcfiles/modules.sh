if [ `id -u` -ne 0 ]; then 
  export MODULEPATH=/cm/local/modulefiles:/cm/shared/modulefiles
  export PATH=${PATH}:/sbin:/usr/sbin
else 
  export MODULEPATH=/cm/local/modulefiles
fi
