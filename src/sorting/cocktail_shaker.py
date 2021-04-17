from sorting.sorter import Sorter

class CocktailShakerSort(Sorter):
    def _bubbleUp(self, items, cutoff):
        swaps = 0
        for j in range(cutoff, self.length - (cutoff+1))[::-1]:
            if items[j + 1] < items[j]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swaps += 1
        return swaps

    def _bubbleDown(self, items, cutoff):
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
            swaps = self._bubbleDown(items, i)
            swaps += self._bubbleUp(items, i)
            i += 1
            
