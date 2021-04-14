import unittest
from sorting.stupidSort import StupidSort
from sorting.insertionSort import InsertionSort
from sorting.opBubbleSort import OpBubbleSort
from sorting.cocktailShaker import CocktailShakerSort
from sorting.mergeSort import MergeSort
from sorting.quickSort import QuickSort

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
        self._sortTestHelper(StupidSort)

    def test_InsertionSort(self):
        self._sortTestHelper(InsertionSort)

    def test_OpBubbleSort(self):
        self._sortTestHelper(OpBubbleSort)

    def test_CocktailShakerSort(self):
        self._sortTestHelper(CocktailShakerSort)

    def test_MergeSort(self):
        self._sortTestHelper(MergeSort)

    def test_QuickSort(self):
        self._sortTestHelper(QuickSort)

            
if __name__ == "__main__":
    unittest.main()
