def is_isogram(string):
    string = string.lower()
    characters = []
    for char in string:
        if char in [' ', '-']:
            continue
        if char in characters:
            return False
        else:
            characters.append(char)
    return True