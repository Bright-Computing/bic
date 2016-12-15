#!/bin/sh

export CWD=`pwd`

if [ -d /usr/src/redhat ]
then export RPMDIR=/usr/src/redhat/SOURCES
else export RPMDIR=/usr/src/packages/SOURCES
fi


NAME=Lmod-files
CMVERSION=7.0

export CWD=`pwd`
cd $CWD

TMPDIR=/tmp/$NAME-build-$RANDOM

cp *.patch $RPMDIR/

mkdir -p $TMPDIR/$NAME-$CMVERSION

cp *.sh $TMPDIR/$NAME-$CMVERSION
cp *.csh $TMPDIR/$NAME-$CMVERSION

cd $TMPDIR
tar -zcvf $RPMDIR/$NAME-$CMVERSION.tar.gz $NAME-$CMVERSION
rm -rf $TMPDIR
