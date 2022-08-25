class Node:
    def __init__(self, count, weight, total_weight):
        self.count = count
        self.weight = weight
        self.total_weight = total_weight
        self.previous = None
        self.edges = []
        self.index = -1
