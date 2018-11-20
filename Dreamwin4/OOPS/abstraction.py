import abc
from abc import abstractmethod, ABCMeta


class Abstract(metaclass=ABCMeta):

    #__metaclass__ = ABCMeta  # python 2
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    def stop(self):
        pass


class Implement(Abstract):

    def start(self):
        return "start the car by pressing the start button"

    def drive(self):
        return "driving the car"


obj = Implement()
print(obj.start())


