from sorting.sorter import Sorter

class InsertionSort(Sorter):
    def sort(self, items, cutoff = None):
        temp = None
        for i in range(1, len(items)):
            temp = items[i]
            j = i - 1
            while j >= 0 and items[j] >= temp:
                items[j], items[j + 1] = items[j + 1], items[j]
                j -= 1
