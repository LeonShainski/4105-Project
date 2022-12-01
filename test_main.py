import main   # The code to test

def test_checkImages():
    assert main.checkImages('4105-Project\images') == ['tire-corrupt.png']

def test_checkImages():
    assert main.checkImages('4105-Project\dataset') == []