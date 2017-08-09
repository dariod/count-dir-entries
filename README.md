This script was developed to help researching the behavior of a certain class users in order to better define a design problem. We needed to know how many files per directory the users deal with.

An example run:
```text
$ python ./countEntries.py ~
Walked through 155563 directories
Mean number of entries per directory: 5.248497
Maximum number of entries in a directory: 35622 (/Users/dario/Library/Caches/Metadata/Safari/History)
```

When during the run CTRL-C is pressed, the stats up to that point are printed:
```text
$ python ./countEntries.py ~
Walked through 1942 directories^C
Mean number of entries per directory: 9.330072
Maximum number of entries in a directory: 776 (/Users/dario/Documents/Projects/test)
```
