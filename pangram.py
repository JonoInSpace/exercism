ALPHABET = 'qwertyuiopasdfghjklzxcvbnm'
def is_pangram(sentence):
    unique_letters = ''
    for letter in sentence.lower():
        if letter in ALPHABET:
            if letter not in unique_letters:
                unique_letters += letter
    if len(unique_letters) == len(ALPHABET):
        return True
    else:
        return False