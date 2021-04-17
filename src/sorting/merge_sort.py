from sorting.sorter import Sorter

class MergeSort(Sorter):
    def sort(self, items, cutoff = None):
        result = self._merge_sort(items)
        self._mutate_list(items, result)

    def _merge_sort(self, items):
        if len(items) <= 1:
            return items
        split = len(items) // 2
        left_list = self._merge_sort(items[:split])
        right_list = self._merge_sort(items[split:])
        return self._merge_lists(left_list, right_list)

    def _merge_lists(self, left_list, right_list):
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
