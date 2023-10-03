import math

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 10

def test_square():
    num = 7
    assert num*num == 80

def test_check():

    x = 100
    assert x>=10099

def test_fun():

    x = 2
    assert x+1 == 5

def test_multiply():

    x = 6
    y = 2
    assert x*y == 18  