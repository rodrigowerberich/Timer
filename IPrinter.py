from abc import ABC, abstractmethod
from typing import AnyStr


class IPrinter(ABC):
    @abstractmethod
    def print(self, string: AnyStr, end: AnyStr):
        pass