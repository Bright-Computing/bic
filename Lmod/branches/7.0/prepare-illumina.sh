#!/bin/sh

export CWD=`pwd`

if [ -d /usr/src/redhat ]
then export RPMDIR=/usr/src/redhat/SOURCES
else export RPMDIR=/usr/src/packages/SOURCES
fi


NAME=Lmod-site-config
CMVERSION=7.0
LMODVERSION=6.1.7

export CWD=`pwd`
cd $CWD

TMPDIR=/tmp/$NAME-build-$RANDOM

mkdir -p $TMPDIR/$NAME-$LMODVERSION-$CMVERSION

cp 00-user_is_root.sh $TMPDIR/$NAME-$LMODVERSION-$CMVERSION


cd $TMPDIR
tar -zcvf $RPMDIR/$NAME-$CMVERSION.tar.gz $NAME-$LMODVERSION-$CMVERSION
rm -rf $TMPDIR
