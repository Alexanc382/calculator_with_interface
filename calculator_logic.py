def add(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):  # имена аргументов могут быть любые
    return a * b


def divide(a, b):
        if b == 0:
            raise ZeroDivisionError('Делить на ноль нельзя!')
        return a / b


def square(a):
    return a ** 2

def cube(a):
    return a ** 3