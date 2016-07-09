import sorter

class StupidSort(sorter.Sorter):
    def sort(self, items, cutoff = None):
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
                i = tel - 1
                tel = 0
            else:
                i += 1
