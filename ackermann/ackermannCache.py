#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys

class AckermannOverflowError(RuntimeError):
    pass

class AckermannCache(object):
    def __init__(self):
        sys.setrecursionlimit(20000)
        self.cache = {}
        self.size = 0
    
    def getAckermann(self, m, n):
        if m in self.cache.keys():
            if n in self.cache[m].keys():
                return self.cache[m][n]
        else:
            self.cache[m] = {}
        result = 0
        try:
            if m < 1:
                result = n + 1
            elif n < 1:
                result = self.getAckermann(m-1, 1)
            else:
                result = self.getAckermann(m-1, self.getAckermann(m, n-1))
        except (RuntimeError):
            raise AckermannOverflowError, "Recursion limit of %s reached" % sys.getrecursionlimit()
        self.cache[m][n] = result
        self.size += 1
        return result

    def __str__(self):
        result = []
        for m in self.cache.keys():
            row = []
            for n in self.cache[m].keys():
                row.append("(%d, %d) = %d" % (m, n, self.cache[m][n]))
            result.append("; ".join(row))
        return "\n".join(result)

    @staticmethod
    def main():
        maxM = 6
        maxN = 6
        arguments = len(sys.argv)
        if arguments == 3:
            maxM = int(sys.argv[1])
            maxN = int(sys.argv[2])
        elif arguments == 2:
            maxN = int(sys.argv[1])
        cache = AckermannCache()
        try:
            for m in range(maxM):
                for n in range(maxN):
                    a = cache.getAckermann(m, n)
                    print "Ackermann(%d, %d) is %d (%d calculations)" % (m, n, a, cache.size)
        except (AckermannOverflowError):
            print cache.size
        except (KeyboardInterrupt):
            sys.exit(0)

if __name__ == "__main__":
    AckermannCache.main()
