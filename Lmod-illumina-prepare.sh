#!/bin/sh

export CWD=`pwd`

RPMDIR=$HOME/rpmbuild/SOURCES
mkdir -p $RPMDIR

NAME=Lmod-files
CMVERSION=8.0

export CWD=`pwd`
cd $CWD
TMPDIR=/tmp/$NAME-build-$RANDOM-$$
cp *.patch $RPMDIR/
mkdir -p $TMPDIR/$NAME-$CMVERSION
cp *.sh *.csh *.lua *.py $TMPDIR/$NAME-$CMVERSION

cd $TMPDIR
tar -zcvf $RPMDIR/$NAME-$CMVERSION.tar.gz $NAME-$CMVERSION
echo $RPMDIR/$NAME-$CMVERSION.tar.gz
rm -rf $TMPDIR
