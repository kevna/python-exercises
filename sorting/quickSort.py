import sorter

class QuickSort(sorter.Sorter):
    def sort(self, items, cutoff = None):
        result = self._quickSort(items)
        for i in range(len(items)):
            items[i] = result[i]
        items.extend(result[len(items):])

    def _quickSort(self, items):
        if len(items) < 2:
            return items
        split = len(items) // 2
        pivot = items[split]
        items.remove(pivot)

        lowList = []
        highList = []

        for i in range(len(items)):
            if items[i] <= pivot:
                lowList.append(items[i])
            else:
                highList.append(items[i])
        if len(lowList) > 1:
            lowList = self._quickSort(lowList)
        if len(highList) > 1:
            highList = self._quickSort(highList)
        return lowList + [pivot] + highList
