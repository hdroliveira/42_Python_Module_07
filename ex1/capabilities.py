from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str = "itself") -> str:
        """Heals the target."""
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.is_transformed = False

    @abstractmethod
    def transform(self) -> str:
        """Transforms the creature."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Reverts the creature to its original form."""
        pass
