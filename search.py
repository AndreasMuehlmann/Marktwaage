from abc import ABCMeta, abstractmethod


class Search(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_closesed(self, number):
        pass

    def set_nodes(self, nodes):
        self.nodes = nodes
