from abc import ABC
from abc import abstractmethod

from fastapi import Response


class Controller(ABC):
    """
    Controller interface.

    This interface defines the methods that must be provided by the
    controllers.
    """

    @abstractmethod
    async def run(self, *args, **kwargs) -> Response:
        raise NotImplementedError
