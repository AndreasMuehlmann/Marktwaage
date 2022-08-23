from get_combinations import get_combinations
from write_tree import write_tree

from linear_search import LinearSearch
from better_linear_search import BetterLinearSearch

from reconstruct_path import reconstruct_path


def run(start_weights, searched_weights):
    nodes = get_combinations(start_weights)
    write_tree(nodes, 'tree_representation.txt')

    results = {}
    search = BetterLinearSearch(nodes)
    for searched_weight in searched_weights:
        closesed = search.get_closesed(searched_weight)
        reconstruct_path(closesed, [])

    return results
