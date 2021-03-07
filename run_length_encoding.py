NUMBERS = '123456789'
def decode(string):
    text = ''
    x = '1'
    num_mode = False
    for char in string:
        if char in NUMBERS:
            if not num_mode:
                x = char
                num_mode = True
            else:
                x = x + char
        else:
            text = text + char * int(x)
            num_mode = False
            x = 1
    return text

def encode(string):
    if string == '':
        return ''
    text = ''
    run_length = 0
    holder = string[0]
    for char in string:
        if char == holder:
            run_length += 1
        else:
            if run_length == 1:
                text += holder
            else:
                text += str(run_length) + holder
            holder = char
            run_length = 1
    if run_length == 1:
        text += holder
    else:
        text += str(run_length) + holder
    return text