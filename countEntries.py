#!/usr/bin/python
import sys
import os
import signal

'''
As walking the filesystem might take time, when user press CTRL-C (SIGINT) print
out partial results.
'''
def handlerSIGINT(signal, frame):
        finalOutput()
        sys.exit(0)

signal.signal(signal.SIGINT, handlerSIGINT)

'''
This is to avoid writing the code twice, this function is used to write out the
summary at the end of the run or when we catch a CTRL-C (SIGINT)
'''
def finalOutput():
    sys.stdout.write("\n")
    sys.stdout.flush()
    print("Mean number of entries per directory: %f") % (avgItemsPerDir)
    print("Maximum number of entries in a directory: %d (%s)") % (maxEntries[1],maxEntries[0])

'''
Get one parameter that is the root of the tree we want to count
'''
rootDir="/"
if len(sys.argv) >= 2:
    rootDir=sys.argv[1]

nDirsWalked=0
avgItemsPerDir=0.0
maxEntries=('',0)

'''
Walk the directory tree and calcuate average (mean) and maximum amount of
entries per directory.
'''
sys.stdout.write(("Walked through %d directories") % (nDirsWalked))
sys.stdout.flush()
for thisDir,subDirs,files in os.walk(rootDir):
    nDirsWalked+=1
    nSubDirs=len(subDirs)
    nFiles=len(files)
    nTot=nSubDirs + nFiles
    if nTot > maxEntries[1]:
        maxEntries=(thisDir,nTot)
    '''
    We do not know the total amount of directories upfront, nor we want to
    sum the total number of entries as that might overflow, we use an
    iterative method to evaluate the mean:
    http://www.heikohoffmann.de/htmlthesis/node134.html
    '''
    avgItemsPerDir+=(nTot - avgItemsPerDir) / nDirsWalked
    sys.stdout.write(("\rWalked through %d directories") % (nDirsWalked))
    sys.stdout.flush()
finalOutput()
