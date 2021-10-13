import copy
import requests
from collections import deque

class Node:

    def __init__(self, value, previous):
        self.id = id 
        self.previous = previous
        self.value = value

    def give_unused_id():
        id = 0
        while True:
            id += 1
            yield id 
            
def get_weigts():
    url = 'https://bwinf.de/fileadmin/user_upload/gewichtsstuecke0.txt'
    result = requests.get(url)
    doc = result.content.decode("utf-8").split()
    weights = []
    for i in range(1, len(doc), 2):
        weights.append([int(doc[i]), int(doc[i + 1])])
    return weights        

def find_combination(weights, searched_weight):
    should_run = True
    visited = []
    queue = deque([Node(0, True, None)])
    while len(queue) != 0 and should_run:
        for node in queue:
            if node.weight == searched_weight:
                should_run = False
                break
            for weight in weights:
                if weight[1] != 0:
                    continue
                queue.append(Node(node.weight + weight[0], True))            
                queue.append(Node(node.weight - weight[0], False))
        visited.append(node.id)

def get_path(start, end, path=[]):
    path.appendleft(end)
    return get_path(end.previous)

def print_combination_for_weight(weight, combination):
    pass

def main():
    #weights = get_weigts()
    weights = [[10, 1], [5, 3]]
    for weight in range(10,20, 10):
        combination = find_combination(weights, weight)
        if combination:
            print_combination_for_weight(weight, combination)
        else:
            print(f'There is no combination for {weight}g')
    return

if __name__ == '__main__':
    main()
