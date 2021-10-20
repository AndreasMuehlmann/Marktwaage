import time
import requests
from collections import deque
import copy

class Node:

    index = None

    def __init__(self, weight, total_weight, previous):
        self.previous = previous
        self.weight = weight
        self.total_weight = total_weight

    def  give_available_weights(self, weights, path):
        deleted_weights = 0
        for node in path:
            for index in range(len(weights)):
                index -= deleted_weights
                if node.weight == weights[index][0]:
                    weights[index][1] -= 1
                    if weights[index][1] == 0:
                        del weights[index] 
                        deleted_weights += 1
        return weights 

def get_weigts():
    url = 'https://bwinf.de/fileadmin/user_upload/gewichtsstuecke0.txt'
    result = requests.get(url)
    doc = result.content.decode("utf-8").split()
    start_weights = []
    for i in range(1, len(doc), 2):
        start_weights.append([int(doc[i]), int(doc[i + 1])]) 
    return start_weights

def get_closesed_weight(searched_weight, visited):
    closesed_weight = visited[0]
    for node in visited:
        if abs(closesed_weight.total_weight - searched_weight) < abs(node.weight - searched_weight):
            closesed_weight = node
    return closesed_weight

def get_path(end, visited, path=[]):
    path = [end] + path
    if  end.previous is None:
        return path
    return get_path(visited[end.previous], visited, path)

def check_if_similar_path_already_there(path, visited):
    path = set(path)
    for node in visited:
        are_similar = set(get_path(node, visited)) == path
        if are_similar: 
            return True
    return False

def reachable(weights, searched_weight, current_weight):
    total = 0
    for weight in weights: 
        for _ in range(weight[1]):
            total += weight[0]
    if total + current_weight < searched_weight:
        return False
    return True

def find_combination(weights, searched_weight):
    visited = []
    queue = deque([Node(0, 0, None)])
    while queue:
        node = queue[0]
        node.index = len(visited)
        path = get_path(node, visited)
        if node.total_weight == searched_weight:
            return path
        #if check_if_similar_path_already_there(path, visited):
        #    del queue[0]
        #    continue
        available_weights = node.give_available_weights(copy.deepcopy(weights), path)
        #if not reachable(weights, searched_weight, node.total_weight): 
        #    continue
        for weight in available_weights: 
            if node.total_weight < searched_weight:           
                queue.append(Node(+weight[0], node.total_weight + weight[0], node.index)) 
            else:
                queue.append(Node(-weight[0], node.total_weight - weight[0], node.index))
        visited.append(queue.popleft())
    return get_path(get_closesed_weight(searched_weight, visited), visited)

def print_path_for_weight(weight , path):
    print(f'weight {weight}:')
    for node in path:
        print(node.weight)

def main():
    weights = get_weigts()
    start = time.time()
    for start_weigths in range(10, 1000, 10):
        path = find_combination(copy.deepcopy(weights), start_weigths)
        if path:
            print_path_for_weight(start_weigths , path)
        else:
            print(f'There is no combination for {start_weigths}g')
    print(f'time: {time.time() - start}')
    return

if __name__ == '__main__':
    main()