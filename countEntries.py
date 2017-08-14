#!/usr/bin/python
import sys
import os
import signal
import argparse
from math import sqrt


'''
Set up argument parsing
'''
parser = argparse.ArgumentParser()
parser.add_argument("--skip", "-s", help="directory name to skip over", action="append", nargs="?")
parser.add_argument("pathname", help="directory to examine", type=str, default=".")
args = parser.parse_args()


'''
As walking the filesystem might take time, when user press CTRL-C (SIGINT) print
out partial results.
'''
def handlerSIGINT(signal, frame):
        finalOutput()
        sys.exit(0)

signal.signal(signal.SIGINT, handlerSIGINT)

'''
The directory class
'''
class directorySummary:

    def __init__(self):
        self.__histogram={}
        self.__maxEntries=('',0)
        self.__meanEntries=0.0
        self.__nDirs=0

    def addDir(self,n,pathname):
        '''
        Update the total numebr of entries added
        '''
        self.__nDirs+=1

        '''
        Update the sumamry histogram
        '''
        if n in self.__histogram:
            self.__histogram[n]+=1
        else:
            self.__histogram[n]=1

        '''
        Update maximum numebr of entries per directory
        '''
        if n > self.__maxEntries[1]:
            if pathname != None:
                self.__maxEntries=(pathname,n)
            else:
                self.__maxEntries=('',n)


        '''
        We do not know the total amount of directories upfront, nor we want to
        sum the total number of entries as that might overflow, we use an
        iterative method to evaluate the mean:
        http://www.heikohoffmann.de/htmlthesis/node134.html
        '''
        self.__meanEntries+=(n - self.__meanEntries) / self.__nDirs

    def nEntries(self):
        return self.__nDirs

    def maxEntries(self):
        return self.__maxEntries

    def meanEntries(self):
        return self.__meanEntries

    def stdDev(self):
        dev=0.0
        if (self.__nDirs > 1):
            for x in self.__histogram:
                dev+=(self.__histogram[x] - self.__meanEntries) ** 2
            dev = sqrt(dev / (self.__nDirs - 1))
        return dev

    def dump(self):
        for n in sorted(self.__histogram):
            print "%d: %d" % (n,self.__histogram[n])

'''
This is to avoid writing the code twice, this function is used to write out the
summary at the end of the run or when we catch a CTRL-C (SIGINT)
'''
def finalOutput():
    sys.stdout.write("\n")
    sys.stdout.flush()
    print("Maximum number of entries in a directory: %d (%s)") % (summary.maxEntries()[1],summary.maxEntries()[0])
    print("Mean number of entries per directory: %f") % (summary.meanEntries())
    print("Standard deviation for the number of entries per directory: %f") % (summary.stdDev())

def skipDir(dir):
    if (args.skip != None) and (dir in args.skip):
        return True
    else:
        return False

rootDir=args.pathname
summary=directorySummary()

'''
Walk the directory tree and calculate average (mean) and maximum amount of
entries per directory.
'''
sys.stdout.write(("Walked through %d directories") % (summary.nEntries()))
sys.stdout.flush()
for thisDir,subDirs,files in os.walk(rootDir,topdown=True):

    '''
    Skip over given directories
    '''
    subDirs[:] = [d for d in subDirs if not skipDir(d)]

    '''
    Get the number of entries for this directory
    '''
    nSubDirs=len(subDirs)
    nFiles=len(files)
    nTot=nSubDirs + nFiles
    summary.addDir(nTot,thisDir)

    sys.stdout.write(("\rWalked through %d directories") % (summary.nEntries()))
    sys.stdout.flush()
finalOutput()
