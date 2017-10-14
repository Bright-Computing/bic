#### Why:  Initiate variable settings in Unix/Linux environments via definitions in YAML, fi. for default $MODULEPATH, LMOD_*, EASYBUILD_* etc
#### Who:  Fotis Georgatos, 2017, MIT license
/bin/bash -c 'ls /etc/profile.definitions/{global*,site/*,nodecategory/*,groups/`id -gn`,user/`id -un`}.yml 2>/dev/null' | setenv PARSEFILES "`cat`"

if ( ! $?__Init_Default_Profile )  then
  foreach file ($PARSEFILES)
    if ( -f $file ) then
      eval `python /etc/profile.d/007-sh-in-it.xyzzy.py $file|sed 's/^export /setenv /g;s/=\(.*\)/ \1/g'|tr '\n' ';'`
    endif
  end
  setenv __Init_Default_Profile 1
endif
