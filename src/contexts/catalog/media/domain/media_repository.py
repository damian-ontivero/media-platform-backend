from abc import ABC
from abc import abstractmethod

from contexts.catalog.media.domain.media import Media
from contexts.shared.domain.criteria.criteria import Criteria


class MediaRepository(ABC):
    """
    Media repository interface.

    This interface defines the methods that must be provided by the
    repository of media.
    """

    @abstractmethod
    def matching(self, criteria: Criteria) -> list[Media]:
        raise NotImplementedError

    @abstractmethod
    def search(self, id: str) -> Media | None:
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def save(self, beer: Media) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
