from sorting.sorter import Sorter, SortList

class OpBubbleSort(Sorter):
    """Implementation of optimised bubble sort.
    Compare the current pair, if they are out of order, swap them then move forward.
    This bubbles the highest value to the end of the list, the next pass is one shorter.
    Optimisation: if no swaps were made everything else is sorted, we can shortcut out.
    """

    def sort(self, items: SortList, cutoff: int = None):
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
