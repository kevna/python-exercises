import unittest
import time
import stupidSort
import insertionSort
import opBubbleSort
import cocktailShaker
import mergeSort
import quickSort

class Test_Sorter(unittest.TestCase):
    BENCHMARKSIZE = 500
    TESTLIST = [([6, 2, 4, 1, 3], [1, 2, 3, 4, 6]),
                ([-5, -1, -3, -10], [-10, -5, -3, -1]),
                (["twelve", "three", "one"], ["one", "three", "twelve"]),
                (["twelve", "three", "one"]*BENCHMARKSIZE, ["one"]*BENCHMARKSIZE + ["three"]*BENCHMARKSIZE + ["twelve"]*BENCHMARKSIZE),
                ]
    def _sortTestHelper(self, testSortObj):
        testSorter = testSortObj()
        for testArgItems, expectedResult in self.TESTLIST:
            actualResult = testArgItems[:]
            timing = time.time()
            result = testSorter.sort(actualResult)
            timing = time.time() - timing
            if result is not None:
                actualResult = result
            self.assertEqual(expectedResult, list(actualResult))
        print "%s\t%.10f" % (testSorter.__class__.__name__, timing)
        
    
    def test_StupidSort(self):
        self._sortTestHelper(stupidSort.StupidSort)

    def test_InsertionSort(self):
        self._sortTestHelper(insertionSort.InsertionSort)

    def test_OpBubbleSort(self):
        self._sortTestHelper(opBubbleSort.OpBubbleSort)

    def test_CocktailShakerSort(self):
        self._sortTestHelper(cocktailShaker.CocktailShakerSort)

    def test_MergeSort(self):
        self._sortTestHelper(mergeSort.MergeSort)

    def test_MergeIterSort(self):
        self._sortTestHelper(mergeSort.MergeIterSort)

    def test_QuickSort(self):
        self._sortTestHelper(quickSort.QuickSort)

    def test_QuickIterSort(self):
        self._sortTestHelper(quickSort.QuickIterSort)

            
if __name__ == "__main__":
    unittest.main()
