import time
from search import Search


class InterpolationSearch(Search):
    def __init__(self):
        self.nodes = []

    def get_closesed(self, number):
        low = 0
        high = len(self.nodes) - 1

        if not self.nodes.any():
            return -1

        while low < high:
            time.sleep(0.1)

            if number <= self.nodes[low]:
                return self.nodes[low]
            elif number >= self.nodes[high]:
                return self.nodes[high]
            
            interpolation = int(low + (number - self.nodes[low]) \
                / (self.nodes[high] - self.nodes[low]) \
                * (high - low))
            print(f'high: {high}, low: {low}, high_val: {self.nodes[high]}, ' \
                  + f'low_val: {self.nodes[low]}, number: {number}, interpolation: {interpolation}, ')

            if self._is_closesed(number, self.nodes[interpolation]):
                self.closesed = self.nodes[interpolation]

            if self.nodes[interpolation] > number:
                print('hello')
                low = interpolation + 1
                print(low)

            elif self.nodes[interpolation] < number:
                high = interpolation - 1

            else:
                return self.closesed

        return self.closesed

    def _is_closesed(self, number, node):
        # return abs(self.closesed.total_weight - number) > \
        #    abs(node.total_weight - number)
        return abs(self.closesed - number) > \
            abs(node - number)

    def set_nodes(self, nodes):
        self.nodes = nodes
        if self.nodes.any():
            # self.nodes.sort(key=lambda node: node.total_weight)
            self.closesed = self.nodes[0]
