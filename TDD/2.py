import unittest

class Dodawanie(unittest.TestCase):
    def test_1(self):
        result = addition(3,6)
        assert result == 9

    def test_2(self):
        result = addition(3,6,1)
        assert result == 10
    
    
def addition(*args):
    total = 0
    for i in args:
        total += i
    
    return total



if __name__ == "__main__":
    unittest.main()