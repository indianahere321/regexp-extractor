import glob
from os import listdir, walk
from os.path import isfile, join
import re
import sys

regexp_patterns = dict()

def is_java_file(f):
    return f.endswith(".java")

def is_android_file(f):
    return f.endswith(".jimple")

def initialize_regexp_patterns():
    global regexp_patterns
    regexp_patterns["-j"] = list()
    regexp_patterns["-j"].append('Pattern\.compile\("([^"]*)"')
    regexp_patterns["-j"].append('matches\("([^"]*)"')
    regexp_patterns["-j"] = '|'.join(regexp_patterns["-j"])

    regexp_patterns["-a"] = list()
    regexp_patterns["-a"].append('java\.util\.regex\.Pattern compile\(java\.lang\.String\)>\("([^"]*)"')
    regexp_patterns["-a"].append('boolean matches\(java\.lang\.String\)>\("([^"]*)"')
    regexp_patterns["-a"] = '|'.join(regexp_patterns["-a"])

def regexp_extraction(path, language):
    global regexp_patterns
    for root, subFolders, files in walk(path):
        for f in files:
            if (language == "-a" and is_android_file(f)) or (language == "-j" and is_java_file(f)):
                file = open(join(root,f),"r")
                for line in file.readlines():
                    matches = re.findall(regexp_patterns[language], line)
                    for tuple in matches:
                        for str in tuple:
                            if str != '':
                                print '"'+str+'"'

if __name__ == '__main__':
    initialize_regexp_patterns()

    if len(sys.argv) == 3:
        path = sys.argv[1]
        language = sys.argv[2]
        if language == "-j" or language == "-a":
            regexp_extraction(path, language)
        else:
            print "Usage: python extract_regexps.py <path> -[a | j]"
    else:
        print "Usage: python extract_regexps.py <path> -[a | j]"

    

