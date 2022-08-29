import time
import os
from multiprocessing import Pool

import numpy as np

from node import Node
from iir_filter import IirFilter

from linear_search import LinearSearch
from better_linear_search import BetterLinearSearch
from binary_search import BinarySearch
from interpolation_search import InterpolationSearch
from interpolated_binary_search import InterpolatedBinarySearch


def create_random_test(length):
    '''
    generating list of nodes:
    nodes = []
    for _ in range(length):
        total_weight = np.random.uniform(-max_val, max_val)
        node = Node(0, 0, total_weight)
        nodes.append(node)
    '''

    # numbers = np.random.uniform(-1, 1, 1000) # uniform distrubtion
    numbers = np.random.rand(length) # normal distribution
    sorted_numbers = np.sort(numbers)
    return sorted_numbers

def time_search_number(search, numbers, number):
    search.set_nodes(numbers)

    start = time.time()
    search.get_closesed(number)

    return time.time() - start

def avg_time_search(length):
    search = InterpolationSearch()

    new_numbers = 5
    searches_per_number = 2000

    results = []
    for new_number in range(new_numbers):
        numbers = create_random_test(length)
        for search_per_number in range(searches_per_number):
            number = np.random.uniform(-1, 1)

            time = time_search_number(search, numbers, number)
            results.append(time)

    avg_time = np.mean(results)
    print(f'length: {length}, avg_time: {round(time * 10**6, 5)}')
    return avg_time

def write_file(search_times, lengths, file_path):
    with open(file_path, 'w') as file:
        file.write('n, mikro_s\n')

        for count, time in enumerate(search_times):
            file.write(f'{lengths[count]},{round(time * 10**6, 5)}\n')

def main():
    lengths = range(0, 3001, 10) # small numbers
    # lengths = range(0, 300001, 1000) # large numbers
    start = time.time()

    counter = 0
    while True:
        if time.time() - start > 5:
            break
        counter += 1

    '''
    multiprocessing
    with Pool() as pool:
        search_times = pool.map(avg_time_search, range(1000000, 10000001, 1000000))
    '''
    search_times = [avg_time_search(length) for length in lengths]

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'interpolation_search_normal_small_numbers.csv'
    file_path = os.path.join(current_dir, 'timer', file_name)
    write_file(search_times, lengths, file_path)


if __name__ == '__main__':
    main()
