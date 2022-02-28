from sorting.sorter import Sorter, SortList

class TimSort(Sorter):  # pylint: disable=too-few-public-methods
    MINIMUM = 32

    def minrun(self, length: int) -> int:
        remainder = 0
        while length >= self.MINIMUM:
            remainder |= length % 2
            length //= 2
        return length + remainder

    def insertion_sort(self, items: SortList, left: int, right: int) -> SortList:
        minj = left-1
        for i in range(left, right):
            temp = items[i]
            j = i - 1
            while j >= minj and items[j] >= temp:
                items[j+1] = items[j]
                j -= 1
            items[j+1] = temp
        return items

    def sort(self, items: SortList, cutoff: int = None) -> SortList:
        length = len(items)
        minrun = self.minrun(length)

        for start in range(1, length, minrun):
            end = min(start+minrun, length)
            self.insertion_sort(items, start, end)

        return items
