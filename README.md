# bic
<b>B</b>right-<b>i</b>llumina <b>c</b>ollaboration

This repository holds prototype versions of Lmod, with improved and modernized `.spec` files,
whereby the sequence of startup scripts under `/etc/profile.d` is kept as generic as possible and
minimal assumptions are made against the delivery environment (ie. sysadmins retain full control of the configuration).

The effort is beyond prototype stage, as of Aug 2017, and is mainly here for testing & refining the RPM generation process.
Typically, the RPM build is just a matter of typing:

  * `time rpmbuild -ba Lmod-illumina.spec`
