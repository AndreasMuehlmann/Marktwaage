from __future__ import annotations
import time
import requests
import copy
from dataclasses import dataclass


@dataclass(order=True)
class Node:
    available_weights : list
    weight : int 
    total_weight : int
    previous : Node
    index : int = None

def get_weigts():
    url = 'https://bwinf.de/fileadmin/user_upload/gewichtsstuecke0.txt'
    result = requests.get(url)
    doc = result.content.decode("utf-8").split()
    start_weights = []
    for i in range(1, len(doc), 2):
        start_weights.append([int(doc[i]), int(doc[i + 1])]) 
    return start_weights

def sort_helper(node):
    return abs(searched_weight - node.total_weight)

def get_closesed_weight(visited):
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

def path_exists(path, visited): # dont use
    for node in visited:
        are_similar = sorted(get_path(node, visited)) == sorted(path)
        if are_similar: 
            return True
    return False

def remove_all_matching_nodes(visited): # dont use
    deleted = 0
    for node_index, node in  enumerate(visited):
        node_index -= deleted
        if path_exists(get_path(node, visited), visited):
            del visited[node_index] 
            deleted += 1
        node.index -= deleted
        node.previous
    return visited

def reachable(weights, current_weight): #dont use
    total = 0
    for weight in weights: 
        for _ in range(weight[1]):
            total += weight[0]
    if total + current_weight < searched_weight:
        return False
    return True

def remove_one_weight(weights, index):
    weights[index][1] -= 1
    if weights[index][1] == 0:
        del weights[index]
    return weights

def find_combination(weights):
    visited = []
    queue = [Node(weights, 0, 0, None)]
    while queue:
        node = queue[0]
        node.index = len(visited)
        if node.total_weight == searched_weight:
            return get_path(node, visited)
        for index, weight in enumerate(node.available_weights): 
            if node.total_weight < searched_weight:           
                queue.append(Node(remove_one_weight(copy.deepcopy(node.available_weights), index), +weight[0], node.total_weight + weight[0], node.index)) 
            else:
                queue.append(Node(remove_one_weight(copy.deepcopy(node.available_weights), index), -weight[0], node.total_weight - weight[0], node.index))
        visited.append(queue[0])
        del queue[0]
        queue.sort(key=sort_helper)
    return get_path(get_closesed_weight(visited), visited)

def print_path_for_weight(path):
    print(f'weight {searched_weight}:')
    for node in path:
        print(node.weight)

def main():
    global searched_weight
    weights = get_weigts()
    start = time.time() 
    for searched_weight in range(10, 1000, 10):
        path = find_combination(copy.deepcopy(weights))
        if path:
            print_path_for_weight(path)
        else:
            print(f'There is no combination for {searched_weight}g')
    print(f'time: {time.time() - start}')
    return

if __name__ == '__main__':
    main()