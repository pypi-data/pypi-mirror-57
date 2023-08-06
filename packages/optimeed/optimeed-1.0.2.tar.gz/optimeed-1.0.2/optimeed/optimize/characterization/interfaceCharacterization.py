from abc import ABCMeta, abstractmethod
from optimeed.core.options import Option_class


class InterfaceCharacterization(Option_class, metaclass=ABCMeta):
    """Interface for the evaluation of a device"""

    @abstractmethod
    def compute(self, theDevice):
        """
        Action to perform to characterize (= compute the objective function) of the machine.

        :param theDevice: the machine to characterize
        """
        pass
