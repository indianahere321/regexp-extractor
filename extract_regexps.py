import glob
from os import listdir, walk
from os.path import isfile, join, isdir
import re
import sys

regexp_patterns = dict()

def is_java_file(f):
    return f.endswith(".java")

def is_jimple_file(f):
    return f.endswith(".jimple")

def post_process(str):
    res = ''
    literal = True
    for i in range(len(str)):
        if str[i] == '"' and (i == 0 or (0 < i and str[i - 1] != '\\')):
            literal = not literal
            continue
        if literal:
            res += str[i]
        elif str[i] != ' ' and str[i] != '+':
            return '';
    return res;

def initialize_regexp_patterns():
    global regexp_patterns
    regexp_patterns["-java"] = list()
    regexp_patterns["-java"].append('Pattern\.compile\("(.*)"')
    regexp_patterns["-java"].append('matches\("(.*)"')
    regexp_patterns["-java"] = '|'.join(regexp_patterns["-java"])

    regexp_patterns["-jimple"] = list()
    regexp_patterns["-jimple"].append('java\.util\.regex\.Pattern compile\(java\.lang\.String\)>\("(.*)"')
    regexp_patterns["-jimple"].append('boolean matches\(java\.lang\.String\)>\("(.*)"')
    regexp_patterns["-jimple"] = '|'.join(regexp_patterns["-jimple"])

def regexp_extraction(path, language):
    global regexp_patterns
    regexs = list()
    for root, subFolders, files in walk(path):
        for f in files:
            if (language == "-jimple" and is_jimple_file(f)) or (language == "-java" and is_java_file(f)):
                file = open(join(root,f),"r")
                for line in file.readlines():
                    matches = re.findall(regexp_patterns[language], line)
                    for tuple in matches:
                        for str in tuple:
                            str = post_process(str);
                            if str != '':
                                regexs.append('"'+str+'"')
    return regexs

def multiple_regexp_extraction(path, language):
    global regexp_patterns
    for f in listdir(path):
        if isdir(f):
            regexs=regexp_extraction(join(path,f), language)
            out = open(f + '.txt', 'w')
            for re in regexs:
                out.write(re + '\n')

if __name__ == '__main__':
    initialize_regexp_patterns()

    if len(sys.argv) == 3:
        path = sys.argv[1]
        language = sys.argv[2]
        if language == "-java" or language == "-jimple":
            multiple_regexp_extraction(path, language)
        else:
            print "Usage: python extract_regexps.py <path> -[java | jimple]"
    else:
        print "Usage: python extract_regexps.py <path> -[java | jimple]"

    

