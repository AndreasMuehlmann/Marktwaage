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

def give_shorter_combination(combination1, combination2):
    if len(combination1) < len(combination2):
        return combination1
    else:
        return combination2

def give_possible_combination(combination1, combination2):
    if combination1 and combination2:
            return give_shorter_combination(combination1, combination2)
    elif combination1:
        return combination1 
    elif combination2:
        return combination2
    else:
        return False        

def call_find_combination_with_the_right_values(weights, searched_weight, weight, combination):
    weights[weight][1] -= 1
    combination1 = find_combination(weights, searched_weight + weights[weight][0], combination + deque([weights[weight][0]]))
    combination2 = find_combination(weights, searched_weight - weights[weight][0], combination + deque([-weights[weight][0]]))
    return combination1, combination2

def find_combination(weights, searched_weight, combination=deque([]), deleted_weights=0):
    if searched_weight == 0:
        return combination
    for weight in range(len(weights)): #give_best weights in order. For that make funktion. 
        weight -= deleted_weights
        weights = copy.deepcopy(weights)
        if weights[weight][1] == 0:
            del weights[weight]
            deleted_weights += 1
            continue 
        combination1, combination2 = call_find_combination_with_the_right_values(weights, searched_weight, weight, combination)
        combination = give_possible_combination(combination1, combination2)
        if combination:
            return combination
    return False

def print_combination_for_weight(weight, combination):
    pass

def main():
    #weights = get_weigts()
    weights = [10, 5]
    count_weights = [1, 3]
    for weight in range(10,20, 10):
        combination = find_combination(weights, weight)
        if combination:
            print_combination_for_weight(weight, combination)
        else:
            print(f'There is no combination for {weight}g')
    return

if __name__ == '__main__':
    main()
