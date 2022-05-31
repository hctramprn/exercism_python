def flatten(iterable):
    flat = []
    for i in iterable:
        if isinstance(i, list):
            flat += flatten(i)
        elif isinstance(i, int):
            flat.append(i)
    return flat
