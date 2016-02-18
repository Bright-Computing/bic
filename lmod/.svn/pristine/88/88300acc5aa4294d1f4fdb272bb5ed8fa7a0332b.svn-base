#!/bin/ksh

. /etc/profile.d/modules.sh

if [ `module load dot 2>&1 | wc -l` != 0 ]
then echo Could not load module \"dot\" using /bin/ksh
     exit 1
fi

if [ `module load shared 2>&1 | wc -l` != 0 ]
then echo Could not load module \"shared\" using /bin/ksh
     exit 1
fi

if [ `module load shared default-ethernet 2>&1 | wc -l` != 0 ]
then echo Could not load module \"default-ethernet\" using /bin/ksh
     exit 1
fi

exit 0
