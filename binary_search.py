from search import Search


class BinarySearch(Search):
    def __init__(self):
        self.nodes = []

    def get_closesed(self, number):
        low = 0
        high = len(self.nodes) - 1
        mid = 0

        if not self.nodes.any():
            return -1

        while low <= high:

            mid = (high + low) // 2

            if self._is_closesed(number, self.nodes[mid]):
                self.closesed = self.nodes[mid]

            if self.nodes[mid] < number:
            # if self.nodes[mid].total_weight < number:
                low = mid + 1
            elif self.nodes[mid] > number:
            # elif self.nodes[mid].total_weight > number:
                high = mid - 1
            else:
                return self.nodes[mid]

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
