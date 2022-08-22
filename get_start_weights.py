
def get_start_weights(path):
    with open(path, 'r') as file:
        text = file.read().split()

    start_weights = []

    for i in range(1, len(text), 2):
        start_weights.append((int(text[i]), int(text[i + 1])))
    return start_weights
