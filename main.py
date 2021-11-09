import time
import requests
from dataclasses import dataclass


@dataclass()
class Node:

    count : int
    weight : int 
    total_weight : int
    index : int
    previous : int = None

    def __post_init__(self):
        self.total_weight += self.count * self.weight


def get_weigts(url):
    result = requests.get(url)
    doc = result.content.decode("utf-8").split()
    start_weights = []

    for i in range(1, len(doc), 2):
        start_weights.append((int(doc[i]), int(doc[i + 1]))) 
    return start_weights

def get_closesed_weight(visited, searched_weight):
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

def get_combinations(weights):
    visited = [Node(0, 0, 0, 0)]
    for weight in weights:
        visited_add_on = []
        for node in visited:
            for count in range(weight[1]):
                    visited_add_on.append(Node(count + 1, +weight[0], node.total_weight, len(visited) + len(visited_add_on), node.index)) 
                    visited_add_on.append(Node(count + 1, -weight[0], node.total_weight, len(visited_add_on) + len(visited), node.index))
        visited.extend(visited_add_on)
    return visited 

def write_path_for_weight_to_file(path, searched_weight, file):
    file.write(f'weight {searched_weight} -> reached weight {path[-1].total_weight}')
    for node in enumerate(path):
        for _ in range(node.count):
            file.write(f'{node.weight}  ')
        file.write('\n')
    file.write('\n')
    return

def main():
    for task in range(6):
        with open(f'marktwaage_results{task}.txt', 'w') as file:
            file.write('Marktwaage\n\n')
            file.write(f'Test {task}\n\n')
            weights = get_weigts(f'https://bwinf.de/fileadmin/user_upload/gewichtsstuecke{task}.txt')

            start = time.time() 
            visited = get_combinations(weights)
            print(f'time get_combinations: {time.time() - start}')

            for searched_weight in range(10, 10010, 10):
                path = get_path(get_closesed_weight(visited, searched_weight), visited)
                write_path_for_weight_to_file(path, searched_weight, file) 

            print(f'time: {time.time() - start}')
    return

if __name__ == '__main__':
    main()