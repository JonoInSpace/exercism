ALPHA = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
def response(hey_bob):
    has_chars = False
    hey_bob = hey_bob.strip()
    if hey_bob:
        for char in ALPHA:
            if char in hey_bob:
                has_chars = True
                break
        if has_chars:
            if hey_bob == hey_bob.upper():
                if hey_bob[-1] == '?':
                    return "Calm down, I know what I'm doing!"
                else:
                    return "Whoa, chill out!"
        if hey_bob[-1] == '?':
            return 'Sure.'
        else:
            return 'Whatever.'
                
    else:
        return 'Fine. Be that way!'
        
                
        
