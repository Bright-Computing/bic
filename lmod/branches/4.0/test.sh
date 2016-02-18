#!/bin/sh

set -e

if [ -e /bin/bash ]
then test_files/modules-test.bash
fi

if [ -e /bin/tcsh ]
then test_files/modules-test.tcsh
     rm -f output
fi

if [ -e /bin/ksh ]
then test_files/modules-test.ksh
fi

# Test if there are any modules which refer to non-existent paths
result=0
. /etc/profile.d/modules.sh
module add shared

for mod in `find /cvos/local/modulefiles/ -type f | cut -d'/' -f5- | grep -v 'use.own' | grep -v 'modules'; find /cvos/shared/modulefiles/ -type f | cut -d'/' -f5-`
do
  for file in `module show $mod 2>&1 | grep -Eo ' /.*' | tr -s ":" "\n"`
  do
    if [ ! -e $file ]; then
      echo "Non existent path in module '$mod':"
      echo "$file"
      echo
      result=1
    fi
  done
done

exit $result
