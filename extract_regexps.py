from os import listdir
from os.path import isfile, join
import re
import sys

if len(sys.argv) == 2:
    path = sys.argv[1]
else:
    path = "."
print "Extracting regexps from path:", path
for f in listdir(path):
    if isfile(join(path,f)):
        file = open(join(path,f),"r")
        for line in file.readlines():
            matches = {e for e in set(re.findall(
                      'java\.util\.regex\.Pattern compile\(java\.lang\.String\)>\("([^"]*)"', line))\
                      | set(re.findall('boolean matches\(java\.lang\.String\)>\("([^"]*)"', line))}
            for str in matches:
                print str
