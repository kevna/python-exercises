from sorting.sorter import Sorter

class CocktailShakerSort(Sorter):
    def __init__(self):
        self.length = 0

    def _bubble_up(self, items, cutoff):
        swaps = 0
        for j in range(cutoff, self.length - (cutoff+1))[::-1]:
            if items[j + 1] < items[j]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swaps += 1
        return swaps

    def _bubble_down(self, items, cutoff):
        swaps = 0
        for j in range(cutoff, self.length - (cutoff+1)):
            if items[j + 1] < items[j]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swaps += 1
        return swaps

    def sort(self, items, cutoff = None):
        swaps = 1
        i = 0
        self.length = len(items)
        while i < self.length / 2 and swaps > 0:
            swaps = self._bubble_down(items, i)
            swaps += self._bubble_up(items, i)
            i += 1
