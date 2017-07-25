#!/bin/sh

export CWD=`pwd`

RPMDIR=$HOME/rpmbuild/SOURCES
if [ -d /usr/src/redhat ]
 then if [ ! -x $RPMDIR ]
  then export RPMDIR=/usr/src/redhat/SOURCES
 fi
fi

NAME=Lmod-files
CMVERSION=7.0

export CWD=`pwd`
cd $CWD

TMPDIR=/tmp/$NAME-build-$RANDOM-$$

cp *.patch $RPMDIR/

mkdir -p $TMPDIR/$NAME-$CMVERSION
cp *.sh $TMPDIR/$NAME-$CMVERSION
cp *.csh $TMPDIR/$NAME-$CMVERSION
cp *.lua $TMPDIR/$NAME-$CMVERSION

cd $TMPDIR
tar -zcvf $RPMDIR/$NAME-$CMVERSION.tar.gz $NAME-$CMVERSION
echo $RPMDIR/$NAME-$CMVERSION.tar.gz
rm -rf $TMPDIR
