#!/usr/bin/python
import sys
import os

# Get one parameter that is the root of the tree we want to count
rootDir="/"
if len(sys.argv) >= 2:
    rootDir=sys.argv[1]

nDirsWalked=0
avgItemsPerDir=0.0
maxEntries=('',0)

# Walk the directory tree and calcuate average and maximum amount of entries oer
# directory.
sys.stdout.write(("Walked through %d directories") % (nDirsWalked))
sys.stdout.flush()
for thisDir,subDirs,files in os.walk(rootDir):
    nDirsWalked+=1
    nSubDirs=len(subDirs)
    nFiles=len(files)
    nTot=nSubDirs + nFiles
    if nTot > maxEntries[1]:
        maxEntries=(thisDir,nTot)
    # We do not know the total amount of directories upfront, nor we want to
    # sum the total number of entries as that might overflow, we use an
    # iterative method to evaluate the mean:
    # http://www.heikohoffmann.de/htmlthesis/node134.html
    avgItemsPerDir+=(nTot - avgItemsPerDir) / nDirsWalked
    sys.stdout.write(("\rWalked through %d directories") % (nDirsWalked))
    sys.stdout.flush()
sys.stdout.write("\n")
sys.stdout.flush()
print("Mean number of entries per directory: %f") % (avgItemsPerDir)
print("Maximum number of entries in a directory: %d (%s)") % (maxEntries[1],maxEntries[0])
