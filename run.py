from linear_search import LinearSearch
from better_linear_search import BetterLinearSearch

from reconstruct_path import reconstruct_path
from get_combinations import get_combinations


def run(start_weights, searched_weights):
    nodes = get_combinations(start_weights)

    results = {}
    search = BetterLinearSearch(nodes)
    for searched_weight in searched_weights:
        closesed = search.get_closesed(searched_weight)
        reconstruct_path(closesed, [])

    return results
