from abc import ABC, abstractclassmethod, abstractmethod


class Observer(ABC):
    @abstractmethod
    def Handle(self) -> None:
        """Does changes after event is fired."""
