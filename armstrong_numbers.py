def is_armstrong_number(number):
    total = 0
    for num in str(number):
        total += int(num) ** len(str(number))
    
    if total == number:
        return True
    return False 