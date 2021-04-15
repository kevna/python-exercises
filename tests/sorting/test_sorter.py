import pytest

from sorting.stupidSort import StupidSort
from sorting.insertionSort import InsertionSort
from sorting.opBubbleSort import OpBubbleSort
from sorting.cocktailShaker import CocktailShakerSort
from sorting.mergeSort import MergeSort
from sorting.quickSort import QuickSort

class TestSorter:
    TESTLIST = (
        ([6, 2, 4, 1, 3], [1, 2, 3, 4, 6]),
        ([-5, -1, -3, -10], [-10, -5, -3, -1]),
        (["twelve", "three", "one"], ["one", "three", "twelve"]),
            )

    def _sortTestHelper(self, testSortObj, testArgItems, expectedResult):
        testSorter = testSortObj()
        actualResult = testArgItems[:]
        testSorter.sort(actualResult)
        assert actualResult == expectedResult

    @pytest.mark.parametrize('testArgItems, expectedResult', TESTLIST)
    def test_StupidSort(self, testArgItems, expectedResult):
        self._sortTestHelper(StupidSort, testArgItems, expectedResult)

    @pytest.mark.parametrize('testArgItems, expectedResult', TESTLIST)
    def test_InsertionSort(self, testArgItems, expectedResult):
        self._sortTestHelper(InsertionSort, testArgItems, expectedResult)

    @pytest.mark.parametrize('testArgItems, expectedResult', TESTLIST)
    def test_OpBubbleSort(self, testArgItems, expectedResult):
        self._sortTestHelper(OpBubbleSort, testArgItems, expectedResult)

    @pytest.mark.parametrize('testArgItems, expectedResult', TESTLIST)
    def test_CocktailShakerSort(self, testArgItems, expectedResult):
        self._sortTestHelper(CocktailShakerSort, testArgItems, expectedResult)

    @pytest.mark.parametrize('testArgItems, expectedResult', TESTLIST)
    def test_MergeSort(self, testArgItems, expectedResult):
        self._sortTestHelper(MergeSort, testArgItems, expectedResult)

    @pytest.mark.parametrize('testArgItems, expectedResult', TESTLIST)
    def test_QuickSort(self, testArgItems, expectedResult):
        self._sortTestHelper(QuickSort, testArgItems, expectedResult)
