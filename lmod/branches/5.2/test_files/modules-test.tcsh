#!/bin/tcsh

source /etc/profile.d/modules.csh

module load dot >& output
if ( `cat output | wc -l` != 0 ) then
  echo Could not load module \"dot\" using /bin/tcsh
  exit 1
endif

module load shared >& output
if ( `cat output | wc -l` != 0 ) then
  echo Could not load module \"shared\" using /bin/tcsh
  exit 1
endif

module load shared default-environment >& output
if ( `cat output | wc -l` != 0 ) then
  echo Could not load module \"default-environment\" using /bin/tcsh
  exit 1
endif

exit 0
