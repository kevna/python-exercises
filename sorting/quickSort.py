import sorter
import itertools

class QuickSort(sorter.Sorter):
    def sort(self, items, cutoff = None):
        return self._quickSort(items)

    def _quickSort(self, items):
        size = len(items)
        if size < 2:
            return items
        pivot = items.pop(size / 2)

        lowList = []
        highList = []

        for item in items:
            if item <= pivot:
                lowList.append(item)
            else:
                highList.append(item)
        return self._quickSort(lowList) + [pivot] + self._quickSort(highList)

class QuickIterSort(QuickSort):
    def _quickSort(self, items):
        size = len(items)
        if size < 2:
            for item in items:
                yield item
        else:
            pivot = items.pop(size / 2)

            low = []
            high = []
            for item in items:
                if item > pivot:
                    high.append(item)
                else:
                    low.append(item)
            for item in itertools.chain(self._quickSort(low), iter([pivot]), self._quickSort(high)):
                yield item
