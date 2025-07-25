def add(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):  # имена аргументов могут быть любые
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка! Делить на ноль нельзя!"

def square(a):
    return a ** 2

def cube(a):
    return a ** 3