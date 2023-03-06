def factorial(number):
    if type(number) is not int:
        return None
    if number < 0:
        return None
    if number == 0:
        return 1
    return number * factorial(number - 1)


print(factorial(3))
