import time
import os
from multiprocessing import Pool

import numpy as np

from node import Node

from linear_search import LinearSearch
from better_linear_search import BetterLinearSearch
from binary_search import BinarySearch
from interpolated_binary_search import InterpolatedBinarySearch


def create_random_test(length, max_val):
    nodes = []
    for _ in range(length):
        total_weight = np.random.uniform(-max_val, max_val)
        node = Node(0, 0, total_weight)
        nodes.append(node)

    return nodes

def time_search_random_number(search, length):
    max_val = 1000

    searched_number = np.random.uniform(-max_val, max_val)
    nodes = create_random_test(length, max_val)
    search.set_nodes(nodes)

    start = time.time()
    search.get_closesed(searched_number)

    return time.time() - start

def avg_time_search(length):
    search = InterpolatedBinarySearch()
    range_avg = 5

    results = []
    for _ in range(range_avg):
        time = time_search_random_number(search, length)
        results.append(time)

    avg_time = np.mean(results)
    print(f'length: {length}, avg_time: {round(time * 10**6, 5)}')
    return avg_time

def write_file(times, file_path):
    with open(file_path, 'w') as file:
        file.write('n, mikro_s\n')

        for count, time in enumerate(times):
            file.write(f'{count},{round(time * 10**6, 5)}\n')

def main():
    with Pool(5) as pool:
        times = pool.map(avg_time_search, range(1000000, 10000001, 1000000))

    file_name = 'test_interpolated_binary_search.csv'
    file_path = os.path.join('timer', file_name)
    write_file(times, file_path)


if __name__ == '__main__':
    main()
