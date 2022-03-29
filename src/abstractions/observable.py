from abc import ABC, abstractmethod
from abstractions.observer import Observer


class Observable(ABC):
    @abstractmethod
    def Subscribe(observer: Observer) -> None:
        """Attach an observer to observable instance"""

    @abstractmethod
    def Unsubscribe(observer: Observer) -> None:
        """Detach an observer to observable instance"""

    @abstractmethod
    def Notify() -> None:
        """Notify all observables"""
