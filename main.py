import copy
import requests
from collections import deque

def get_weigts():
    url = 'https://bwinf.de/fileadmin/user_upload/gewichtsstuecke0.txt'
    result = requests.get(url)
    doc = result.content.decode("utf-8").split()
    weights = []
    for i in range(1, len(doc), 2):
        weights.append([int(doc[i]), int(doc[i + 1])])
    return weights   

def find_combination(weights, searched_weight):
    closesed_weight = None
    return

def print_combination_for_weight(weight, combination):
    print(f'weight {weight}:')
    for step in combination:
        print(step)
    
def main():
    #weights = get_weigts()
    weights = [
        [10, 1], [5, 3]
        ]
    for weight in range(10,20, 10):
        combination = find_combination(weights, weight)
        if combination:
            print_combination_for_weight(weight[0], combination)
        else:
            print(f'There is no combination for {weight}g')
    return

if __name__ == '__main__':
    main()