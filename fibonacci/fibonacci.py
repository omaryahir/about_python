
import unittest 

def fibonacci():
    a, b = 0, 1
    output = [a]
    for i in range(10):
        a, b = b, a + b 
        output.append(a) 

    print(output)
    return output

class TestFibonacci(unittest.TestCase):

    # expected output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... 
    def test_sequence(self):
        output = fibonacci() 
        self.assertEqual(output[0], 0)
        self.assertEqual(output[1], 1)
        self.assertEqual(output[2], 1)
        self.assertEqual(output[3], 2)
        self.assertEqual(output[4], 3)

if __name__ == '__main__':
    print("Testing ...")
    unittest.main()
    
    

