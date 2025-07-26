import calculator_logic as c

def test_add(): # тестируем сложение
    assert c.add(5, 10) == 15
    assert c.add(4, -2) == 2
    assert c.add(-2, -3) == -5


def test_subtraction(): # тестируем вычитание
    assert c.subtraction(5, 10) == -5
    assert c.subtraction(4, -2) == 6
    assert c.subtraction(-2, -3) == 1
    assert c.subtraction(10, 5) == 5


def test_multiply(): # тестируем умножение
    assert c.multiply(5, 5) == 25
    assert c.multiply(5, -3) == -15
    assert c.multiply(-3, -3) == 9



