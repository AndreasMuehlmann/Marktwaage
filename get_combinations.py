from node import Node


def get_combinations(weights):
    nodes = [Node(0, 0, 0)]
    for weight in weights:
        nodes_add_on = []
        for node in nodes:
            for count in range(weight[1]):
                edge = Node(count + 1, +weight[0], node.total_weight, node)
                node.edges.append(edge)
                nodes_add_on.append(edge)

                edge = Node(count + 1, -weight[0], node.total_weight, node)
                node.edges.append(edge)
                nodes_add_on.append(edge)

        nodes.extend(nodes_add_on)
    return nodes
