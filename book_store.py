def has_books(basket):
    if basket == []:
        return False
    for book in basket:
        if book in [1,2,3,4,5]:
            return True
    return False

def build_biggest_set(books):
    biggest_set = []
    for i in range(len(books)):
        book = books[i]
        if book not in biggest_set and book != 'X':
            biggest_set.append(book)
            books[i] = 'X'
        
        print(books)
    return biggest_set
        
def build_sets(basket):
    sets = []
    while has_books(basket):    
        sets.append(build_biggest_set(basket))
    return sets

def get_fours(sets):
    fives = 0
    threes = 0
    fours = 0
    for group in sets:
        if len(group) == 3:
            threes += 1
        elif len(group) == 5:
            fives += 1
    while (fives > 0 and threes > 0):
        fours += 1
        fives -= 1
        threes -= 1
    return fours

def total(basket):
    total = 0
    sets = build_sets(basket)
    fours_needed = get_fours(sets)
    for group in sets:
        L = len(group)
        if L == 1:
            total += 800
        elif L == 2:
            total += 1520
        elif L == 3:
            total += 2160
        elif L == 4:
            total += 2560
        elif L == 5:
            total += 3000
    if fours_needed > 0:
        total -= 40 * fours_needed
    return total