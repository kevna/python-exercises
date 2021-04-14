class Sorter(object):
    def _mutateList(self, subject, update):
        overwrite = len(subject)
        for i in range(overwrite):
            subject[i] = update[i]
        subject.extend(update[overwrite:])

    def sort(self, items, cutoff = None):
        pass
