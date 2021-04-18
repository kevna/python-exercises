import sorter

class QuickSort(sorter.Sorter):
    def sort(self, items, cutoff = None):
        result = self._quickSort(items)
        self._mutateList(items, result)

    def _quickSort(self, items):
        if len(items) < 2:
            return items
        split = len(items) // 2
        pivot = items[split]
        items.remove(pivot)

        lowList = []
        highList = []

        for item in items:
            if item <= pivot:
                lowList.append(item)
            else:
                highList.append(item)
        if len(lowList) > 1:
            lowList = self._quickSort(lowList)
        if len(highList) > 1:
            highList = self._quickSort(highList)
        return lowList + [pivot] + highList
