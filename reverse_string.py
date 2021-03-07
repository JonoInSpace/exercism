def reverse(text):
    txet= ''
    for i in range(len(text)):
        txet += text[-1-i]
    return txet