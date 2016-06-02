# regexp-extractor
A Python script for extracting regular expressions from Java source code or Java bytecode (in Soot's Jimple format).

## Usage
<p align="center">
python extract_regexps.py <path> -[java | jimple] -[single | multiple]
</p>
where:
* \<path\> is the path of the directory containing the files.
* -java and -jimple correspond to whether files to be analyzed are Java source code or Jimple, respectively.
* -single and -multiple correspond to whether the path contains all the 
files of a single application, or multiple directories with 
different applications, respectively.

The results are written to the file **regexes.txt** in *single* mode, 
and a txt file for each application name in *multiple* mode.