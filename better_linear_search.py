from search import Search


class BetterLinearSearch(Search):
    '''
    This only works for a sorted list when searched
    number is always bigger than the last one.
    '''

    def __init__(self, nodes):
        self.nodes = nodes
        self.nodes.sort(key=lambda node: node.total_weight)

        self.closesed = self.nodes[0]

        # where the positive numbers start
        self.search_start = len(self.nodes) // 2

    def get_closesed(self, number):
        for index in range(self.search_start, len(self.nodes)):
            if self._is_closesed(number, index):
                self.closesed = self.nodes[index]
                self.search_start = index

            elif self.nodes[index].total_weight > self.closesed.total_weight:
                return self.closesed

        return self.closesed

    def _is_closesed(self, number, index):
        return abs(self.closesed.total_weight - number) > \
            abs(self.nodes[index].total_weight - number)
