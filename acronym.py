ALPHABET = 'QWERTYUIOPASDFGHJKLZXCVBNM'

def abbreviate(words):
    words = words.replace('-', ' ')
    acr = ''
    for word in words.split():
        for char in word.upper():
            if char in ALPHABET:
                acr += char
                break
    return acr