#!/usr/bin/python2
# -*- coding: utf-8 -*-
import unittest
from ackermann.ackermannCache import AckermannCache

class Test_Ackerman(unittest.TestCase):
    def test_getAckermann(self):
        testList = (
            (-1, -1, 0),
            (0, 0, 1),
            (0, 5, 6),
            (0, 10, 11),
            (1, 0, 2),
            (1, 5, 7),
            (1, 10, 12),
            (2, 0, 3),
            (2, 5, 13),
            (3, 0, 5),
            (3, 5, 253),
            (4, 0, 13),
            (4, 1, 65533),
                )
        testCache = AckermannCache()
        for testArgM, testArgN, expectedResult in testList:
            actualResult = testCache.getAckermann(testArgM, testArgN)
            self.assertEqual(expectedResult, actualResult)

if __name__ == "__main__":
    unittest.main()
