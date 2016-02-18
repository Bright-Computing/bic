#!/bin/sh

export CWD=`pwd`

if [ -d /usr/src/redhat ]
then export RPMDIR=/usr/src/redhat/SOURCES
else export RPMDIR=/usr/src/packages/SOURCES
fi

export URL=`grep ^Source: modules.spec | sed s/'Source: '//g`

cd $RPMDIR
wget -N $URL

cd $CWD
cp destdir.patch $RPMDIR

mkdir temp1 temp2
cp -a default-modules temp1
diff -ruN temp2 temp1 > ${RPMDIR}/default-modules.patch
rm -rf temp1 temp2

mkdir temp1 temp2
cp -a rcfiles temp1
diff -ruN temp2 temp1 > ${RPMDIR}/rcfiles.patch
rm -rf temp1 temp2
