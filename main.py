import os

from timer import Timer

from run import run
from write_file import write_results


SEARCHED_START = 10
SEARCHED_END = 10000
SEARCHED_STEP = 10
SEARCHED_WEIGHTS = range(SEARCHED_START,
                         SEARCHED_END + 10, SEARCHED_STEP)


def read_start_weights(path):
    with open(path, 'r') as file:
        text = file.read().split()

    start_weights = []

    for i in range(1, len(text), 2):
        start_weights.append((int(text[i]), int(text[i + 1])))
    return start_weights


def main():
    for task in range(6):
        test = f'official{task}.txt'
        path = os.path.join('examples', test)
        start_weights = read_start_weights(path)

        timer = Timer(test)
        timer.start()
        results = run(start_weights, SEARCHED_WEIGHTS)
        timer.stop()
        timer.write_std_out()

        file_path = os.path.join('results', test)
        write_results(results, file_path)


if __name__ == '__main__':
    main()
