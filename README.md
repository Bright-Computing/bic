# bic
<b>B</b>right-<b>i</b>llumina <b>c</b>ollaboration

This repository holds prototype versions of Lmod, with improved and modernized `.spec` files,
whereby startup scripts sequence under `/etc/profile.d` is as generic as possible and
minimal assumptions are made against the delivery environment (ie. sysadmins retain full control of the how).

The effort is beyond prototype stage, as of Aug 2017, and is mainly here for testing & refining the RPM generation process.
Typically, the RPM build is just a matter of typing:
* LMOD_FULL_SETTARG_SUPPORT=yes time rpmbuild -ba Lmod-illumina.spec
