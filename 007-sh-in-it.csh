/bin/bash -c 'ls /etc/profile.definitions/{global*,site/*,nodecategory/*,groups/`id -gn`,user/`id -un`}.yml 2>/dev/null' | setenv PARSEFILES "`cat`"

if ( ! $?__Init_Default_Profile )  then
  foreach file ($PARSEFILES)
    if ( -f $file ) then
      eval `python /etc/profile.d/007-sh-in-it.xyzzy.py $file|sed 's/^export /setenv /g;s/=\(.*\)/ \1/g'|tr '\n' ';'`
    endif
  end
  setenv __Init_Default_Profile 1
endif
