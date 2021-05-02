from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional


SortItems = TypeVar('SortItems')
SortList = list[SortItems]


class Sorter(Generic[SortItems], ABC):
    """Abstract parent for implementing sorting algorithms.
    This allows us to have a defined interface which wouldn't be possible
    if they were only matching functions.
    """

    @staticmethod
    def _mutate_list(subject: SortList, update: SortList):
        """Helper which mutates the sorted results into the original list.
        This is because our current interface is to mutate the original list
        rather than returning the sorted list.
        """
        overwrite = len(subject)
        for i in range(overwrite):
            subject[i] = update[i]
        subject.extend(update[overwrite:])

    @abstractmethod
    def sort(self, items: SortList, cutoff: Optional[int] = None):
        """Provide sorting functionality.
        This method is to be overridden by sorting implementations.
        """
