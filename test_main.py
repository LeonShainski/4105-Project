import main   

#Testing images which include corrpt images, should have one corrupt image of a tire being found
def test_checkImages():
    assert main.checkImages('4105-Project\images') == ['tire-corrupt.png']

#Testing without corrupt images, should recieve empty array
def test_checkImages():
    assert main.checkImages('4105-Project\dataset') == []