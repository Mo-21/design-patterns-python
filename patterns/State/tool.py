from abc import ABC, abstractmethod

"""
Equals the State class in the book
"""


class Tool(ABC):

    @abstractmethod
    def mouse_up(self):
        pass

    @abstractmethod
    def mouse_down(self):
        pass
