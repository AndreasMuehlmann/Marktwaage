import requests
from collections import deque
import copy

class Node:

    def __init__(self, weight, total_weight, previous):
        self.id = id(self)
        self.previous = previous
        self.weight = weight
        self.total_weight = total_weight

    def  give_available_weights(self, weights, path):
        deleted_weights = 0
        for weight in path:
            for index in range(len(weights)):
                index -= deleted_weights
                if weight == weights[index][0]:
                    weights[index][1] -= 1
                    if weights[index][1] == 0:
                        del weights[index] 
                        deleted_weights += 1
        return weights 

def get_weigts():
    url = 'https://bwinf.de/fileadmin/user_upload/gewichtsstuecke0.txt'
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
    path = [end.weight] + path
    for node in visited:
        if node.id == end.previous:
            return get_path(node, visited, path)
    return path

def check_if_similar_path_already_there(path, visited):
    for node in visited:
        if node.total_weight == sum(path):
            are_similar = set(get_path(node, visited)) == set(path)
            if are_similar: 
                return True
    return False

def find_combination(start_weights, searched_weight):
    visited = []
    queue = deque([Node(0, 0, None)])
    while queue:
        node = queue[0]
        path = get_path(node, visited)
        if check_if_similar_path_already_there(path, visited):
            del queue[0]
            continue
        weights = node.give_available_weights(copy.deepcopy(start_weights), path)
        if node.total_weight == searched_weight:
            return path
        for weight in weights: 
            queue.append(Node(+weight[0], node.total_weight + weight[0], node.id)) 
            if node.total_weight > searched_weight:           
                queue.append(Node(-weight[0], node.total_weight - weight[0], node.id))
        visited.append(queue.popleft())
    return get_path(get_closesed_weight(searched_weight, visited), visited)

def print_path_for_weight(weight , path):
    print(f'weight {weight}:')
    for weight in path:
        print(weight)

def main():
    weights = get_weigts()
    for weight in range(10, 10000, 10):
        path = find_combination(copy.deepcopy(weights), weight)
        if path:
            print_path_for_weight(weight , path)
        else:
            print(f'There is no combination for {weight}g')
    return

if __name__ == '__main__':
    main()