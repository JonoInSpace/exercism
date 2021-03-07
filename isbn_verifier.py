def is_valid(isbn):
    check_sum = 0
    isbn_no_dashes = ''
    for char in isbn:
        if char != '-':
            isbn_no_dashes += char
    if len(isbn_no_dashes) != 10:
        return False
    else:
        for i in range(10):
            digit = isbn_no_dashes[i]
            if digit in '0123456789':
                digit = int(digit)
            elif i != 9 or digit != 'X':
                return False
            else:
                digit = 10
            check_sum += (10 - i) * digit
        return check_sum % 11 == 0