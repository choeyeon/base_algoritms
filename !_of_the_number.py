number = int(input("number? = "))

def factorial(number):
    if number == 0:
        return 1

    f = 1
    i = 0

    while i < number:
        i += 1
        f = f * i
    
    return f

print(factorial(number))
