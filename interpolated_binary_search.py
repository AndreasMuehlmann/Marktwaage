from search import Search


class InterpolatedBinarySearch(Search):
    def __init__(self, nodes):
        self.nodes = nodes
        self.nodes.sort(key=lambda node: node.total_weight)

        self.closesed = self.nodes[0]

    def get_closesed(self, number):
        low = 0
        high = len(self.nodes) - 1

        while low < high:
            interpolation = low + abs(number - self.nodes[low].total_weight) \
                / abs(self.nodes[high].total_weight - self.nodes[low].total_weight) \
                * (high - low)
            interpolation = round(interpolation)

            if interpolation <= 0:
                return self.nodes[0]
            elif interpolation >= len(self.nodes):
                return self.nodes[-1]

            if self._is_closesed(number, self.nodes[interpolation]):
                self.closesed = self.nodes[interpolation]

            if self.nodes[interpolation].total_weight > number:
                mid = int((interpolation + high) / 2)

                if number <= self.nodes[mid].total_weight:
                    low = interpolation + 1
                    high = mid
                else:
                    low = mid + 1

            elif self.nodes[interpolation].total_weight < number:
                mid = int((interpolation + low) / 2)

                if number >= self.nodes[mid].total_weight:
                    low = mid
                    high = interpolation - 1
                else:
                    high = mid - 1

            else:
                return self.closesed

        return self.closesed

    def _is_closesed(self, number, node):
        return abs(self.closesed.total_weight - number) > \
            abs(node.total_weight - number)
