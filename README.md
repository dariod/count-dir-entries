This script was developed to help researching the behavior of a certain class users in order to better define a design problem. We needed to know how many files per directory the users deal with.

$ python ./countEntries.py -h
usage: countEntries.py [-h] [--skip [SKIP]] [--csv] pathname

positional arguments:
  pathname              directory to examine

optional arguments:
  -h, --help            show this help message and exit
  --skip [SKIP], -s [SKIP]
                        directory name to skip over
  --csv, -csv           print a CSV summary. Suppresses other output.


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

Specifying --csv suppresses other output and just prints out a CSV list of the number of entries per directory and their frequency, useful for plotting charts:
```text
$ python ./countEntries.py  --csv /var
n.Entries per directory,Frequency
0,8107
1,1759
2,781
3,489
4,247
5,119
6,75
7,76
8,64
9,40
10,29
11,37
12,18
13,12
14,15
15,6
17,9
20,5
21,2
22,3
23,4
24,8
27,5
28,3
31,1
32,5
34,7
35,34
36,5
37,3
38,1
40,2
42,2
43,4
44,1
49,4
52,4
53,3
54,2
58,1
62,1
64,1
65,2
66,2
68,1
89,2
90,2
93,2
100,2
114,1
119,1
122,1
161,1
192,2
225,1
241,1
251,1
257,1
377,1
643,1
1225,1
2478,1
```
