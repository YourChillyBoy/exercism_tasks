def is_armstrong_number(number):
    square = len(str(number))
    result = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        result += digit ** square
        temp = temp // 10
    return result == number
