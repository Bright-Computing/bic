if [ `id -u` -ne 0 ]; then 
  export MODULEPATH=/cvos/local/modulefiles:/cvos/shared/modulefiles
else 
  export MODULEPATH=/cvos/local/modulefiles
fi

