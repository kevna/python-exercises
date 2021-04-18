from sorting.sorter import Sorter

class QuickSort(Sorter):
    """Implementation of quick sort.
    Pick a pivot, divide the list into lower and higher values and sort them
    finally add them together with the pivot.

    Pivot is picked naively using the middle item of the list which could belong
    at one end of the list, reducing efficiency.
    """
    def sort(self, items, cutoff = None):
        result = self._quick_sort(items)
        self._mutate_list(items, result)

    def _quick_sort(self, items):
        if len(items) < 2:
            return items
        split = len(items) // 2
        pivot = items[split]
        items.remove(pivot)

        low_list = []
        high_list = []

        for item in items:
            if item <= pivot:
                low_list.append(item)
            else:
                high_list.append(item)
        if len(low_list) > 1:
            low_list = self._quick_sort(low_list)
        if len(high_list) > 1:
            high_list = self._quick_sort(high_list)
        return low_list + [pivot] + high_list
