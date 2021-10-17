import requests
from collections import deque
import copy

class Node:

    def __init__(self, availabel_weights, weight, total_weight, previous):
        self.id = id(self)
        self.previous = previous
        self.weight = weight
        self.total_weight = total_weight
        self.available_weights = availabel_weights

    def  give_available_weights(self):
        for weight in self.available_weights:
            if weight[0] == self.weight:
                weight[1] -= 1
            if weight[1] == 0:
                del weight
        return self.available_weights

def get_weigts():
    url = 'https://bwinf.de/fileadmin/user_upload/gewichtsstuecke1.txt'
    result = requests.get(url)
    doc = result.content.decode("utf-8").split()
    weights = []
    for i in range(1, len(doc), 2):
        weights.append([int(doc[i]), int(doc[i + 1])])
    return weights   

def get_closesed_weight(searched_weight, visited):
    closesed_weight = visited[0]
    for node in visited:
        if abs(closesed_weight.total_weight - searched_weight) < abs(node.weight - searched_weight):
            closesed_weight = node
    return closesed_weight

def get_path(end, visited, path=[]):
    path = [end] + path
    for node in visited:
        if node.id == end.previous:
            return get_path(node, visited, path)
    return path

def  give_available_weights(weights):
    for weight in weights:
        weight[1] -= 1
        if weight[1] == 0:
            del weight
    return weights

def find_combination(weights, searched_weight):
    visited = []
    queue = deque([Node(weights, 0, 0, None)])
    while queue:
        visited.append(queue[0])
        node = queue.popleft()
        weights = node.give_available_weights()
        if node.total_weight == searched_weight:
            return get_path(node, visited)
        for weight in weights: 
            queue.append(Node(node.available_weights, +weight[0], node.total_weight + weight[0], node.id)) 
            if node.total_weight > searched_weight:           
                queue.append(Node(node.available_weights, -weight[0], node.total_weight - weight[0], node.id))
    return get_path(get_closesed_weight(searched_weight, visited), visited)

def print_path_for_weight(weight , path):
    print(f'weight {weight}:')
    for node in path:
        print(node.weight)

def main():
    weights = get_weigts()
    for weight in range(10, 1000, 10):
        path = find_combination(copy.deepcopy(weights), weight)
        if path:
            print_path_for_weight(weight , path)
        else:
            print(f'There is no combination for {weight}g')
    return

if __name__ == '__main__':
    main()