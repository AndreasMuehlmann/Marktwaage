def write_tree(nodes, file_path):
    define_nodes(nodes, file_path)
    write_all_edges(nodes, file_path)

def define_nodes(nodes, file_path):
    with open(file_path, 'a') as file:
        for index, node in enumerate(nodes):
            file.write(node.weight)
            node.index = index

def write_all_edges(nodes, file_path):
    with open(file_path, 'a') as file:
        for node in nodes:
            for edge in node.edges:
                file.write(f'{node.index} > {edge.index}')
