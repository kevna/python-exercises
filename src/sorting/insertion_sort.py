from sorting.sorter import Sorter

class InsertionSort(Sorter):
    """Implementation of insertion sort.
    Take each item and move it to where it belongs in the sorted list ahead of it.
    """
    def sort(self, items, cutoff = None):
        temp = None
        for i in range(1, len(items)):
            temp = items[i]
            j = i - 1
            while j >= 0 and items[j] >= temp:
                items[j], items[j + 1] = items[j + 1], items[j]
                j -= 1
