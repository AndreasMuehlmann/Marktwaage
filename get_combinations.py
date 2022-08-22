from node import Node


def get_combinations(weights):
    visited = [Node(0, 0, 0)]
    for weight in weights:
        visited_add_on = []
        for node in visited:
            for count in range(weight[1]):
                visited_add_on.append(Node(count + 1, +weight[0], node.total_weight, node))
                visited_add_on.append(Node(count + 1, -weight[0], node.total_weight, node))
        visited.extend(visited_add_on)
    return visited
