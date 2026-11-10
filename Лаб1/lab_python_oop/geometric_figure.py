from abc import ABC, abstractmethod


class GeometricFigure(ABC):
    @abstractmethod
    def area(self):
        """Return the area of the figure."""

    @classmethod
    def get_name(cls):
        return cls.name
