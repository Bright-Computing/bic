#!/bin/env python
#### Why:  Initiate variable settings in Unix/Linux environments via definitions in YAML, fi. for default $MODULEPATH, LMOD_*, EASYBUILD_* etc
#### Who:  Fotis Georgatos, 2017, MIT license
#### How:  If you can't state your case in oneliner functions, probably you haven't understood it well enough; and if that doesn't work, well, the same!

def unpack(dct, prefix=''):                             ## the below enforces "value", ie. provide double quotes
  if dct is None: return [{'__Elvis_was_here__': '"__Elvis_has_left_the_building__"'}] ## mark in env something went amiss; TBD.
  return [unpack(v, prefix + k + '_') if type(v) == dict else {prefix + k: '"%s"' % str(v)} for k, v in dct.items()]

def flatten(l):                                         ## flatten lists of lists etc
  return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]

def shell_out(dct, (prefix, sep) = ('export ', '=')):   ## prepare strings for consumption by shell (i.e. var definitions)
  return [prefix + k + sep + v for k,v in dict(d.items()[0] for d in dct).items()]

"""
## Surprise, surprise; this worked pretty OK first time - just try in a python interpreter:
##
## >>> data = {'output': {'file': 'yes'}, 'GLOBAL': {'DEBUG': 'yes', 'DEBUGGING': {'DETAILED': 'no', 'HEADER': 'debugging started'}, 'VERBOSE': 'no'}}
## >>> shell_out(flatten(unpack(data)), 'setenv ', ' ')
## ['setenv GLOBAL_DEBUG yes', 'setenv output_file yes', 'setenv GLOBAL_VERBOSE no', 'setenv GLOBAL_DEBUGGING_DETAILED no', 'setenv GLOBAL_DEBUGGING_HEADER debugging started']
## >>> shell_out(flatten(unpack(data)))
## ['export GLOBAL_DEBUG=yes', 'export output_file=yes', 'export GLOBAL_VERBOSE=no', 'export GLOBAL_DEBUGGING_DETAILED=no', 'export GLOBAL_DEBUGGING_HEADER=debugging started']
"""

## from ruamel import yaml ## modern YAML importer, N.B. cannot handle double quotes really well, so it affects unpack() function
import yaml ## == YAML importer, mangles yes->True, N.B. cannot handle double quotes really well, so it affects unpack() function, too!
import fnmatch
import os
import sys

## Ideally, we'd like something like pattern='/etc/profile.definitions/{global*,site/*,nodecategory/*,groups/`id -gn`,user/`id -un`}.yml'
pattern='test/etc/profile.definitions/*.yml' if len(sys.argv)<2 else ' '.join(sys.argv[1:]) ## this is actually directory-recursive, which is counter-intuitive

matches = []
for (root, dirnames, filenames) in os.walk(os.path.dirname(pattern)):
  for filename in fnmatch.filter(filenames, os.path.basename(pattern)):
    what = os.path.join(root, filename)
    if os.path.exists(what) and os.stat(what).st_size and os.access(what, os.R_OK):
      matches.append(what)

shell_knobs = ('setenv ', ' ') if os.path.splitext(sys.argv[0])[1] == '.csh' else ('export ', '=')
for name in matches:
  for rule in shell_out(flatten(unpack(yaml.safe_load(open(name)))), shell_knobs):
    print rule
