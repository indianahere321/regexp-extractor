# regexp-extractor
A Python script for extracting regular expressions from decompiled Java code (in Soot's Jimple format)

## Usage
<p align="center">
python extract_regexps.py <path> -[a | j]
</p>
where <path> is the path of the directory containing the files, and -a and -j correspond 
to whether the source code is in Android or Java, respectively.