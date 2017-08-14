This script was developed to help researching the behavior of a certain class users in order to better define a design problem. We needed to know how many files per directory the users deal with.

$ python ./countEntries.py -h
usage: countEntries.py [-h] [--skip [SKIP]] pathname

positional arguments:
  pathname              directory to examine

optional arguments:
  -h, --help            show this help message and exit
  --skip [SKIP], -s [SKIP]
                        directory name to skip over


An example run:
```text
$ python ./countEntries.py /Users/dario/Downloads/
Walked through 28 directories
Maximum number of entries in a directory: 53 (/Users/dario/Downloads/)
Mean number of entries per directory: 6.107143
```

When during the run CTRL-C is pressed, the stats up to that point are printed:
```text
$ python ./countEntries.py ~/Documents/Projects/
Walked through 907 directories^C
Maximum number of entries in a directory: 299 (/Users/dario/Documents/Projects/mesa/src/compiler/glsl/glcpp/tests)
Mean number of entries per directory: 10.650496
Standard deviation for the number of entries per directory: 12.187871
```

You can specify a directory name to skip (this feature needs improvement): a directory matching exactly the name given (no wildcards yet) will be skipped over:
```text
$ python ./countEntries.py --skip lib --skip tmp /var
Walked through 11285 directories
Maximum number of entries in a directory: 2476 (/var/db/receipts)
Mean number of entries per directory: 3.750908
Standard deviation for the number of entries per directory: 12.187871
```
```text
$ python ./countEntries.py --skip tmp --skip db /var
Walked through 11483 directories
Maximum number of entries in a directory: 1225 (/var/folders/3f/shsh51yd4ps6ml8nspl7fyj40000gn/C/com.apple.IconServices)
Mean number of entries per directory: 3.494383
Standard deviation for the number of entries per directory: 12.187871
```
