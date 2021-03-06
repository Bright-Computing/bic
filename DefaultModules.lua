-- System wide default modules that get loaded
-- This is referenced by LMOD_SYSTEM_DEFAULT_MODULES

function chomp(s)
  s = string.gsub(s, '^%s+', '')
  s = string.gsub(s, '%s+$', '')
  s = string.gsub(s, '[\n\r]+', ' ')
  return s
end

local uid, status = chomp(capture("/usr/bin/id -u"))

if uid == "0" then
  load("shared", "cmd", "cmsh", "cluster-tools", "slurm")
else
  load("shared") -- DEFAULT_MODULES_OTHER
end
