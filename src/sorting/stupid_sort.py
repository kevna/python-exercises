from sorting.sorter import Sorter, SortList


class StupidSort(Sorter):  # pylint: disable=too-few-public-methods
    """Implementation of stupid sort, also known as gnome sort.
    If the current pair are out of order swap them and move back one
    otherwise step forward.
    """

    def sort(self, items: SortList, cutoff: int = None):
        items = items[:]
        tel = 0
        i = 0
        while i < len(items) - 1:
            if items[i + 1] < items[i]:
                if tel == 0:
                    tel = i
                items[i + 1], items[i] = items[i], items[i + 1]
                if  i > 0:
                    i -= 1
            elif tel > 0:
                # Once we've shuffled an item back into place this jumps forward
                # to where we found the out-of order pair (we already checked in between)
                i = tel - 1
                tel = 0
            else:
                i += 1
        return items
