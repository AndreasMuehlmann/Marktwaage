from search import Search


class LinearSearch(Search):
    def __init__(self, nodes):
        self.nodes = nodes
        self.closesed = self.nodes[0]

    def get_closesed(self, number):
        self.closesed = self.nodes[0]
        for node in self.nodes:
            if self._is_closesed(number, node):
                self.closesed = node

        return self.closesed

    def _is_closesed(self, number, node):
        return abs(self.closesed.total_weight - number) > \
            abs(node.total_weight - number)
