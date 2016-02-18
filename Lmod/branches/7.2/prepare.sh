#!/bin/sh

export CWD=`pwd`

if [ -d /usr/src/redhat ]
then export RPMDIR=/usr/src/redhat/SOURCES
else export RPMDIR=/usr/src/packages/SOURCES
fi

NAME=Lmod
VERSION=$(grep "^%define version " ${NAME}.spec | awk '{print $3}')
URL=http://dev.brightcomputing.com/src/${NAME}/${NAME}-${VERSION}.tar.bz2

cd $RPMDIR
wget -N $URL

cd $CWD
# cp -p *.patch $RPMDIR

