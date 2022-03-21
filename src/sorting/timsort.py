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

    def merge(self, items: SortList, left: int, mid: int, right: int) -> SortList:
        if right <= mid:
            return items

        items_left = [items[i] for i in range(left, mid)]
        items_right = [items[i] for i in range(mid, right)]

        pointer = left

        while items_left and items_right:
            if items_left[0] <= items_right[0]:
                new = items_left.pop(0)
            else:
                new = items_right.pop(0)
            items[pointer] = new
            pointer += 1

        if items_left:
            for new in items_left:
                items[pointer] = new
                pointer += 1
        else:
            for new in items_right:
                items[pointer] = new
                pointer += 1

        return items

    def sort(self, items: SortList, cutoff: int = None) -> SortList:
        length = len(items)
        minrun = self.minrun(length)

        for start in range(1, length, minrun):
            end = min(start+minrun, length)
            self.insertion_sort(items, start, end)

        size = minrun
        while size < length:
            double = size * 2
            for left in range(0, length, double):
                mid = min(length, left+size)
                right = min(length, left+double)
                self.merge(items, left, mid, right)
            size = double

        return items
