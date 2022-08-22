import numpy as np

from timer import Timer
from node import Node

from linear_search import LinearSearch
from better_linear_search import BetterLinearSearch
from binary_search import BinarySearch
from interpolated_binary_search import InterpolatedBinarySearch


# TODO: less x-data + bigger sizes


def create_random_test(length, max_val):
    nodes = []
    for _ in range(length):
        total_weight = np.random.uniform(-max_val, max_val)
        node = Node(0, 0, total_weight)
        nodes.append(node)

    return nodes


def main():
    max_val = 1000
    range_average = 10
    timer = Timer('test_binary_search.csv')
    for i in range(1000000, 1000001):
        print(i)
        for _ in range(range_average):
            nodes = create_random_test(i, max_val)
            search = BinarySearch(nodes)
            searched_number = np.random.uniform(-max_val, max_val)
            timer.start()
            search.get_closesed(searched_number)
            timer.stop()
        timer.average(range_average)

    timer.write_file()


if __name__ == '__main__':
    main()
