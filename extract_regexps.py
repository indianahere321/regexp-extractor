from os import listdir
from os.path import isfile, join
import re

path = "."
for f in listdir(path):
    if isfile(f):
        file = open(f,"r")
        for line in file.readlines():
            matches = {e for e in set(re.findall(
                      'java\.util\.regex\.Pattern compile\(java\.lang\.String\)>\("([^"]*)"', line))\
                      | set(re.findall('boolean matches\(java\.lang\.String\)>\("([^"]*)"', line))}
            for str in matches:
                print str
