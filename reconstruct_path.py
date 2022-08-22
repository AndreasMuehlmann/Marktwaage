def reconstruct_path(end, path):
    path = [end] + path
    if end.previous is None:
        return path
    return reconstruct_path(end.previous, path)
