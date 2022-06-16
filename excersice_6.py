def fibonacci(steps):
    numbers = [1]
    a = 0
    b = 1
    for y in range(steps-1):
        c = a + b
        a = b
        b = c
        numbers.append(b)
    return numbers
