import pytest

from sorting.stupid_sort import StupidSort
from sorting.insertion_sort import InsertionSort
from sorting.bubble_sort import OpBubbleSort
from sorting.cocktail_shaker import CocktailShakerSort
from sorting.merge_sort import MergeSort
from sorting.quick_sort import QuickSort
from sorting.timsort import TimSort

class TestSorter:
    TESTLIST = (
        ([6, 2, 4, 1, 3], [1, 2, 3, 4, 6]),
        ([-5, -1, -3, -10], [-10, -5, -3, -1]),
        (['twelve', 'three', 'one'], ['one', 'three', 'twelve']),
        (list(range(41, 0, -1)), list(range(1, 42))),
    )

    def _sort_helper(self, sorter_class, items, expected):
        sorter = sorter_class()
        actual = sorter.sort(items)
        assert actual == expected

    @pytest.mark.parametrize('items, expected', TESTLIST)
    def test_stupid_sort(self, items, expected):
        self._sort_helper(StupidSort, items, expected)

    @pytest.mark.parametrize('items, expected', TESTLIST)
    def test_insertion_sort(self, items, expected):
        self._sort_helper(InsertionSort, items, expected)

    @pytest.mark.parametrize('items, expected', TESTLIST)
    def test_bubble_sort(self, items, expected):
        self._sort_helper(OpBubbleSort, items, expected)

    @pytest.mark.parametrize('items, expected', TESTLIST)
    def test_cocktail_shaker_sort(self, items, expected):
        self._sort_helper(CocktailShakerSort, items, expected)

    @pytest.mark.parametrize('items, expected', TESTLIST)
    def test_merge_sort(self, items, expected):
        self._sort_helper(MergeSort, items, expected)

    @pytest.mark.parametrize('items, expected', TESTLIST)
    def test_quick_sort(self, items, expected):
        self._sort_helper(QuickSort, items, expected)

    @pytest.mark.parametrize('items, expected', TESTLIST)
    def test_timsort(self, items, expected):
        self._sort_helper(TimSort, items, expected)
