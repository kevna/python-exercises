import unittest
import stupidSort
import insertionSort
import opBubbleSort
import cocktailShaker
import mergeSort
import quickSort

class Test_Sorter(unittest.TestCase):
    TESTLIST = (
        ([6, 2, 4, 1, 3], [1, 2, 3, 4, 6]),
        ([-5, -1, -3, -10], [-10, -5, -3, -1]),
        (["twelve", "three", "one"], ["one", "three", "twelve"]),
            )
    def _sortTestHelper(self, testSortObj):
        testSorter = testSortObj()
        for testArgItems, expectedResult in self.TESTLIST:
            actualResult = testArgItems[:]
            testSorter.sort(actualResult)
            self.assertEqual(expectedResult, actualResult)
        
    
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

    def test_QuickSort(self):
        self._sortTestHelper(quickSort.QuickSort)

            
if __name__ == "__main__":
    unittest.main()
