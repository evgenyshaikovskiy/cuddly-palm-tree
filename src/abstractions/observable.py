from abc import ABC, abstractmethod
from abstractions.observer import Observer


class Observable(ABC):
    @abstractmethod
    def Subscribe(self, observer: Observer) -> None:
        """Attach an observer to observable instance"""

    @abstractmethod
    def Unsubscribe(self, observer: Observer) -> None:
        """Detach an observer to observable instance"""

    @abstractmethod
    def Notify(self) -> None:
        """Notify all observables"""
