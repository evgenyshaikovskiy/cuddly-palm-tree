from abc import ABC, abstractclassmethod, abstractmethod


class Observer(ABC):
    @abstractmethod
    def Handle():
        """Does changes after event is fired."""
