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

def square(first):
    return first ** 2

def cube(first):
    return first ** 3