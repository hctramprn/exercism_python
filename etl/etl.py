def transform(legacy_data):
    scrabble = {}
    for key in legacy_data:
        for char in legacy_data[key]:
            scrabble[char.lower()] = key
    return scrabble
