import glob
from os import listdir, walk
from os.path import isfile, join
import re
import sys

def android_regexp_extraction(path):
    for root, subFolders, files in walk(path):
        for f in files:
            if f.endswith(".jimple"):
                file = open(join(root,f),"r")
                for line in file.readlines():
                    matches = {e for e in set(re.findall(\
                               'java\.util\.regex\.Pattern compile\(java\.lang\.String\)>\("([^"]*)"', line))\
                               | set(re.findall('boolean matches\(java\.lang\.String\)>\("([^"]*)"', line))}
                    for str in matches:
                        print '"'+str+'"'

def java_regexp_extraction(path):
    for root, subFolders, files in walk(path):
        for f in files:
            if f.endswith(".java"):
                file = open(join(root,f),"r")
                for line in file.readlines():
                     matches = {e for e in set(re.findall('Pattern\.compile\("([^"]*)"', line))\
                               | set(re.findall('matches\("([^"]*)"', line))}
                     for str in matches:
                         print '"'+str+'"'

if __name__ == '__main__':
    if len(sys.argv) == 3:
        path = sys.argv[1]
        language = sys.argv[2]
        if language == "java":
            java_regexp_extraction(path)
        elif language == "android":
            android_regexp_extraction(path)
        else:
            print "Usage: python extract_regexps.py <path> [android | java]"
    else:
        print "Usage: python extract_regexps.py <path> [android | java]"

    

