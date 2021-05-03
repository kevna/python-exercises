from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional


SortItems = TypeVar('SortItems')
SortList = list[SortItems]


class Sorter(Generic[SortItems], ABC):  # pylint: disable=too-few-public-methods
    """Abstract parent for implementing sorting algorithms.
    This allows us to have a defined interface which wouldn't be possible
    if they were only matching functions.
    """

    @abstractmethod
    def sort(self, items: SortList, cutoff: Optional[int] = None) -> SortList:
        """Provide sorting functionality.
        This method is to be overridden by sorting implementations.
        """
