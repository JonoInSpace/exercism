def rotate(text, key):
    ciphertext = ''
    for char in text:
        char_index = ord(char)
        if char_index in range(65,91)  or char_index in range(97,123):
            shift = 65 + 32*char.islower()
            char_index = ((char_index - shift + key) % 26) + shift
        ciphertext += chr(char_index)
    return ciphertext