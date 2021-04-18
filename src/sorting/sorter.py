class Sorter:
    """Abstract parent for implementing sorting algorithms.
    This allows us to have a defined interface which wouldn't be possible
    if they were only matching functions.
    """

    def _mutate_list(self, subject, update):
        """Helper which mutates the sorted results into the original list.
        This is because our current interface is to mutate the original list
        rather than returning the sorted list.
        """
        overwrite = len(subject)
        for i in range(overwrite):
            subject[i] = update[i]
        subject.extend(update[overwrite:])

    def sort(self, items, cutoff = None):
        """Provide sorting functionality.
        This method is to be overridden by sorting implementations.
        """
