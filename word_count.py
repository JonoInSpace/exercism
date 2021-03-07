PUNCTUATION = ' ,.;:?!()"\n\t'
ALPHABET = 'qwertyuiopasdfghjklzxcvbnm'
NUMBERS = '7410852963'


def split(phrase):
    phrase = phrase.lower()
    word = ''
    words = []
    i = 0
    
    for char in phrase:
        
        if char in ALPHABET or char in NUMBERS:
           word += char
        elif char == "'":
            if phrase[i-1] in ALPHABET:
                if i+1 < len(phrase):
                    if phrase[i+1] in ALPHABET:
                        word += char
        else:
            words.append(word)
            word = ''
            
        i += 1
    words.append(word)
    
    while('' in words):
        words.remove('')
    return words
       
def count_words(sentence):
    words = {}
    sen = split(sentence)
    for word in sen:
        if word not in words:
            words.update({word:0})
        words.update({word:words[word]+1})
    return words
