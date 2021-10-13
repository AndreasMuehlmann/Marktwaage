import requests
from collections import deque

class Node:

    def __init__(self, weight, total_weight, previous):
        self.id = id 
        self.previous = previous
        self.weight = weight
        self.total_weight = total_weight
    
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

def get_closesed_weight(searched_weight, visited):
    closesed_weight = 0
    for weight in visited:
        if abs(closesed_weight - searched_weight) < abs(weight.value - searched_weight):
            closesed_weight = weight
    return closesed_weight

def find_combination(weights, searched_weight):
    visited = []
    queue = deque([Node(0, True, None)])
    while len(queue) != 0:
        for node in queue:
            if node.weight == searched_weight:
                return get_path(node, visited)
            for weight in weights:
                if weight[1] == 0:
                    continue
                queue.append(Node(node.weight + weight[0], True))            
                queue.append(Node(node.weight - weight[0], False))
            visited.append(queue.popleft())
    closesed_weight = get_closesed_weight(visited, searched_weight)
    return get_path(closesed_weight, visited)

def get_path(end, visited, path=[]):
    path.appendleft(end)
    for node in visited:
        if node.id == end.previous:
            path.appendleft(node.weight)
            return get_path(0, node, path)
    return path

def print_path_for_weight():
    pass

def main():
    #weights = get_weigts()
    weights = [[10, 1], [5, 3]]
    for weight in range(10,20, 10):
        path = find_combination(weights, weight)
        if path:
            print_path_for_weight(weight, path)
        else:
            print(f'There is no combination for {weight}g')
    return

if __name__ == '__main__':
    main()
