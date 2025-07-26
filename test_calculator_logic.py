import calculator_logic as c
import pytest


def test_add(): # тестируем сложение
    assert c.add(5, 10) == 15
    assert c.add(4, -2) == 2
    assert c.add(-2, -3) == -5

    with pytest.raises(TypeError):
        c.add('text', 5)
    with pytest.raises(TypeError):
        c.add(5, 'text')


def test_subtraction(): # тестируем вычитание
    assert c.subtraction(5, 10) == -5
    assert c.subtraction(4, -2) == 6
    assert c.subtraction(-2, -3) == 1
    assert c.subtraction(10, 5) == 5

    with pytest.raises(TypeError):
        c.subtraction('text', 5)
    with pytest.raises(TypeError):
        c.subtraction(5, 'text')


def test_multiply(): # тестируем умножение
    assert c.multiply(5, 5) == 25
    assert c.multiply(5, -3) == -15
    assert c.multiply(-3, -3) == 9

    # with pytest.raises(TypeError): || при умножение это не нужно
    #     c.multiply('text', 5)  || текст пропишется 5 раз
    # with pytest.raises(TypeError):
    #     c.multiply(5, 'text')


def test_divide(): # тестируем деление
    assert c.divide(10, 5) == 2
    assert c.divide(-10, 2) == -5
    assert c.divide(-6, -3) == 2

    with pytest.raises(TypeError):
        c.divide('text', 5)
    with pytest.raises(TypeError):
        c.divide(5, 'text')

    with pytest.raises(ZeroDivisionError):
        c.divide(10, 0)


def test_square(): # тестируем возведение в степень 2
    assert c.square(2) == 4
    assert c.square(-2) == 4
    assert c.square(0) == 0

    with pytest.raises(TypeError):
        c.square('text')


def test_cube(): # тестируем возведение в степень 3
    assert c.cube(2) == 8
    assert (c.cube(-2) == -8)
    assert c.cube(0) == 0

    with pytest.raises(TypeError):
        c.cube('text')


test_add()
test_subtraction()
test_multiply()
test_divide()
test_square()
test_cube()
print('Тестирование прошло успешно')