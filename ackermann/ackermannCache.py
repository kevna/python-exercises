#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys

class AckermannOverflowError(RuntimeError):
    pass

class AckermannCache(object):
    CACHEFILE = "cacheFile.dat"
    
    def __init__(self):
        sys.setrecursionlimit(25000)
        self.cache = {}
        self.size = 0
        self.readSize = 0

    def addCache(self, m, n, value):
        try:
            self.cache[m]
        except KeyError:
            self.cache[m] = {}
        self.cache[m][n] = value
        self.size += 1

    def getCache(self, m, n):
        try:
            result = self.cache[m][n]
        except KeyError:
            result = False
        return result

    def loadCache(self, fileName):
        with open(fileName) as fileHandle:
            for line in fileHandle:
                cacheLine = line.strip().split(",")
                m, n, value = cacheLine
                self.addCache(int(m), int(n), int(value))
        self.readSize = self.size

    def saveCache(self, fileName):
        if self.size <= self.readSize:
            return
        with open(fileName, "w") as fileHandle:
            for m in self.cache.keys():
                for n in self.cache[m].keys():
                    print >> fileHandle, "%d,%d,%d" % (m, n, self.cache[m][n])

    def getAckermann(self, m, n):
        result = self.getCache(m, n)
        if result:
            return result
        result = 0
        try:
            if m < 1:
                result = n + 1
            elif n < 1:
                result = self.getAckermann(m-1, 1)
            else:
                result = self.getAckermann(m-1, self.getAckermann(m, n-1))
            self.addCache(m, n, result)
        except (RuntimeError):
            raise AckermannOverflowError, "Recursion limit of %s reached calculating Ackermann(%d, %d)" % (sys.getrecursionlimit(), m, n)
        return result

    def __str__(self):
        result = []
        for m in self.cache.keys():
            row = []
            for n in self.cache[m].keys():
                row.append("(%d, %d) = %d" % (m, n, self.cache[m][n]))
            result.append("; ".join(row))
        return "\n".join(result)

    def ackermannGrid(self):
        maxM = 6
        maxN = 6
        arguments = len(sys.argv)
        if arguments > 2:
            maxM = int(sys.argv[1])
            maxN = int(sys.argv[2])
        elif arguments == 2:
            maxN = int(sys.argv[1])
        for m in range(maxM):
            for n in range(maxN):
                a = self.getAckermann(m, n)
                print "Ackermann(%d, %d) is %d" % (m, n, a)

    def ackermannTo(self):
        maxA = 65533
        arguments = len(sys.argv)
        if arguments > 1:
            maxA = int(sys.argv[1])
        m = 0
        a = 0
        while a < maxA or m < maxA:
            m += 1
            n = 0
            a = 0
            while a < maxA:
                n += 1
                a = self.getAckermann(m, n)
            print "Ackermann(%d, %d) is %d" % (m, n, a)
    
    @staticmethod
    def main():
        cache = AckermannCache()
        cache.loadCache(AckermannCache.CACHEFILE)
        try:
            cache.ackermannTo()
        except (AckermannOverflowError):
            print cache.size
        except (KeyboardInterrupt):
            sys.exit(0)
        cache.saveCache(AckermannCache.CACHEFILE)

if __name__ == "__main__":
    AckermannCache.main()
