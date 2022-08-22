def write_results(results, file_path):
    with open(file_path, 'w') as file:
        for searched_weight, node_path in results.items():
            file.write(f'weight {searched_weight} -> reached weight '
                       + f'{node_path[-1].total_weight}')
            write_path(node_path, file)
            file.write('\n')


def write_path(node_path, file):
    for node in node_path:
        for _ in range(node.count):
            file.write(f'{node.weight}  ')
        file.write('\n')
