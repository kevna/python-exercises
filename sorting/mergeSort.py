import sorter
import itertools

class MergeSort(sorter.Sorter):
    def sort(self, items, cutoff = None):
        return self._mergeSort(items)

    def _mergeSort(self, items):
        size = len(items)
        if size <= 1:
            return items
        split = size / 2
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

class MergeIterSort(MergeSort):
    def _mergeSort(self, items):
        size = len(items)
        if size < 2:
            for item in items:
                yield item
        else:
            split = size / 2
            left = self._mergeSort(items[:split])
            right = self._mergeSort(items[split:])
            for item in self._mergeLists(left, right):
                yield item

    def _mergeLists(self, left, right):
        last = "right"
        try:
            leftTop = next(left)
            rightTop = next(right)
            while True:
                if leftTop < rightTop:
                    yield leftTop
                    last = "left"
                    leftTop = next(left)
                else:
                    yield rightTop
                    last = "right"
                    rightTop = next(right)
        except StopIteration as e:
            if last == "left":
                yield rightTop
                remaining = right
            else:
                yield leftTop
                remaining = left
            for item in remaining:
                yield item
