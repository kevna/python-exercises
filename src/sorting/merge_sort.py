from sorting.sorter import Sorter, SortList

class MergeSort(Sorter):
    """Implementation of merge sort.
    Divide the list in half, sort each half and merge them in order.
    """

    def sort(self, items: SortList, cutoff: int = None) -> SortList:
        items = items[:]
        return self._merge_sort(items)

    def _merge_sort(self, items: SortList) -> SortList:
        if len(items) <= 1:
            return items
        split = len(items) // 2
        left_list = self._merge_sort(items[:split])
        right_list = self._merge_sort(items[split:])
        return self._merge_lists(left_list, right_list)

    def _merge_lists(self, left_list: SortList, right_list: SortList) -> SortList:
        left_offset, right_offset = (0, 0)
        left_len = len(left_list)
        right_len = len(right_list)
        result = []
        while left_offset < left_len and right_offset < right_len:
            if left_list[left_offset] < right_list[right_offset]:
                result.append(left_list[left_offset])
                left_offset += 1
            else:
                result.append(right_list[right_offset])
                right_offset += 1
        result += left_list[left_offset:] + right_list[right_offset:]
        return result
