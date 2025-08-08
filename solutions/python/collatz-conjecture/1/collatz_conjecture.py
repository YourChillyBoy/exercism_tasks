def steps(number):
    steps = 0
    temp = number
    if number < 1:
         raise ValueError("Only positive integers are allowed")
    while temp > 1:
        if temp % 2 == 0:
            temp = temp / 2
            steps += 1
        else:
            temp = temp * 3 + 1
            steps += 1
    return steps
