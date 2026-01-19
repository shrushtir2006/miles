FROM kilometers import miles_to_kilometers

def test_case1():
    assert miles_to_kilometers(5) == "Miles:5\n Kilometers: 8.0467"

def test_case2():
    assert miles_to_kilometers(10) == "Miles:10\n Kilometers: 16.0934"

def test_case3():
    assert miles_to_kilometers(0) == "Miles:0\n Kilometers: 0.0"