NUMBERS =       '0123456789'
SUMOFDOUBLE =   '0246813579'

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num
        self.num = ''.join([num for num in self.card_num if num in NUMBERS])

    def valid(self):
        if len(self.num) <= 1:
            return False
        for char in self.card_num:
            if char not in NUMBERS and char != ' ':
                return False
        else:
            total = 0
            otherdigit = False
            for i in range(len(self.num)-1, -1, -1):
                if otherdigit: 
                    total += int(SUMOFDOUBLE[int(self.num[i])])
                else:
                    total += int(self.num[i])
                otherdigit = (not otherdigit)
                
            if total % 10 == 0:
                return True
            else:
                return False