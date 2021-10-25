import time
import requests
import copy
from dataclasses import dataclass


@dataclass()
class Node:

    count : int
    weight : int 
    total_weight : int
    previous : int = None 
    index : int = None

    def __post_init__(self):
        self.total_weight += self.count * self.weight


def get_weigts():
    url = 'https://bwinf.de/fileadmin/user_upload/gewichtsstuecke4.txt'
    result = requests.get(url)
    doc = result.content.decode("utf-8").split()
    start_weights = []
    for i in range(1, len(doc), 2):
        start_weights.append((int(doc[i]), int(doc[i + 1]))) 
    return start_weights

def get_closesed_weight(visited):
    closesed_weight = visited[0]
    for node in visited:
        if abs(closesed_weight.total_weight - searched_weight) > abs(node.total_weight - searched_weight):
            closesed_weight = node
    return closesed_weight

def get_path(end, visited, path=[]):
    path = [end] + path
    if  end.previous is None:
        return path
    return get_path(visited[end.previous], visited, path)

def find_combination(weights):
    layer = [Node(0, 0, 0)]
    visited = []
    for weight in weights:
        next_layer = [Node(0, 0, 0)]
        for node in layer:
            node.index = len(visited)
            for count in range(weight[1]):
                    next_layer.append(Node(count + 1, +weight[0], node.total_weight, node.index)) 
                    next_layer.append(Node(count + 1, -weight[0], node.total_weight, node.index))
            visited.append(node)
        layer = copy.deepcopy(next_layer)
    visited.extend(next_layer)
    return visited 

def print_path_for_weight(path):
    print(f'weight {searched_weight}:')
    for node in path:
        for count in range(node.count):
            print(node.weight)
    print(f'reached weight{node.total_weight}')

def main():
    global searched_weight
    searched_weight = float('inf')
    weights = get_weigts()
    start = time.time() 
    visited = find_combination(weights)
    end_find_combination = time.time()
    for searched_weight in range(10, 10010, 10):
        path = get_path(get_closesed_weight(visited), visited)
        print_path_for_weight(path) 
    print(f'time: {time.time() - start}')
    print(f'time find_combination: {end_find_combination - start}')
    return

if __name__ == '__main__':
    main()