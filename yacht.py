"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = None
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    
    dice = sorted(dice)
    print(dice)
    
    if category == YACHT:
        holder = dice[0]
        for die in dice:
            if die == holder:
                continue
            else:
                return 0
        return 50
    
    elif category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        total = 0
        for die in dice:
            if die == category:
                total += category
        return total
    
    elif category == FULL_HOUSE:
        # if contains 2 unique rolls
        # and a triplet
        rolls = []
        for die in dice:
            if die not in rolls:
                rolls.append(die)
        if len(rolls) != 2:
            return 0
        else:
            holder = rolls[0]
            count = 0
            for die in dice:
                if die == holder:
                    count += 1
            if count not in [2,3]:
                return 0
            else:
                return sum(dice)
                
    
    elif category == FOUR_OF_A_KIND:
        count = 1
        holder = dice[0]
        
        if dice[1] != dice[0]:
            holder = dice[1]
        else:
            count += 1
        for i in range(2,5):
            if dice[i] == holder:
                count += 1
        if count < 4:
            return 0
        else:
            return 4 * holder
            
    elif category == LITTLE_STRAIGHT:
        if dice == [1,2,3,4,5]:
            return 30
        else:
            return 0
    
    elif category == BIG_STRAIGHT:
        if dice == [2,3,4,5,6]:
            return 30
        else:
            return 0
    
    elif category == CHOICE:
        return sum(dice) 