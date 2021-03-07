SONG = [
            "twelve Drummers Drumming, ",
            "eleven Pipers Piping, ",
            "ten Lords-a-Leaping, ",
            "nine Ladies Dancing, ",
            "eight Maids-a-Milking, ",
            "seven Swans-a-Swimming, ",
            "six Geese-a-Laying, ",
            "five Gold Rings, ",
            "four Calling Birds, ",
            "three French Hens, ",
            "two Turtle Doves, ",
            "and a Partridge in a Pear Tree."
        ]

HEADER = 'On the - day of Christmas my true love gave to me: '

def nth(n):
  #######
    
    if n == 1 : return 'first'
    if n == 2 : return 'second'
    if n == 3 : return 'third'
    if n == 4 : return 'fourth'
    if n == 5 : return 'fifth'
    if n == 6 : return 'sixth'
    if n == 7 : return 'seventh'
    if n == 8 : return 'eighth'
    if n == 9 : return 'ninth'
    if n == 10: return 'tenth'
    if n == 11: return 'eleventh'
    if n == 12: return 'twelfth'
    
    
def recite(start_verse, end_verse):
    if start_verse > end_verse:
        raise Exception('That doesn\'t make sense!')
    verse = ''
    verses = []
    current_verse = start_verse
    if start_verse == 1 and end_verse == 1:
        verses = HEADER.replace('-', f'{nth(1)}') + 'a Partridge in a Pear Tree.'
        return [verses]
    
    else:
        while( current_verse <= end_verse):
            verse = ''
            print(current_verse)
            if current_verse == 1:
                verse += HEADER.replace('-', f'{nth(1)}') + 'a Partridge in a Pear Tree.'
            else:
                verse += ''.join([HEADER.replace('-', f'{nth(current_verse)}')])                   
                verse += ''.join([SONG[-n] for n in range(current_verse,0,-1)])
            current_verse += 1
            verses.append(verse)   
    return verses
    
print(recite(4,7))