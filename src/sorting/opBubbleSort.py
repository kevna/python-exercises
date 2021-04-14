import sorter

class OpBubbleSort(sorter.Sorter):
    def sort(self, items, cutoff = None):
        swaps = 1
        i = 1
        length = len(items)
        while i < length and swaps > 0:
            swaps = 0
            for j in range(length - i):
                if items[j + 1] < items[j]:
                    items[j], items[j + 1] = items[j + 1], items[j]
                    swaps += 1
            i += 1
