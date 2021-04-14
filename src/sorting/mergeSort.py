from sorting.sorter import Sorter

class MergeSort(Sorter):
    def sort(self, items, cutoff = None):
        result = self._mergeSort(items)
        self._mutateList(items, result)

    def _mergeSort(self, items):
        if len(items) <= 1:
            return items
        split = len(items) // 2
        leftList = self._mergeSort(items[:split])
        rightList = self._mergeSort(items[split:])
        return self._mergeLists(leftList, rightList)

    def _mergeLists(self, leftList, rightList):
        leftOffset, rightOffset = (0, 0)
        leftLen = len(leftList)
        rightLen = len(rightList)
        result = []
        while leftOffset < leftLen and rightOffset < rightLen:
            if leftList[leftOffset] < rightList[rightOffset]:
                result.append(leftList[leftOffset])
                leftOffset += 1
            else:
                result.append(rightList[rightOffset])
                rightOffset += 1
        result += leftList[leftOffset:] + rightList[rightOffset:]
        return result
