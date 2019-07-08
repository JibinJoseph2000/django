from python import calculate
def test_calculate():
    percent = calculate(100,10)
    assert percent == 10
    a = "10"
    b = "0"
    percent = calculate(a,b)
    assert percent =="Invalid"
