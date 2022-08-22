from abc import ABCMeta, abstractmethod


class Search(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, nodes):
        pass

    @abstractmethod
    def get_closesed(self, number):
        pass
