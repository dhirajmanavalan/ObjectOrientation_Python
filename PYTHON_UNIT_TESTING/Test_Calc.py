import unittest
import Calc

class test_Calc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calc.add(5,10),15)
        self.assertEqual(Calc.add(5,11),16)
        self.assertEqual(Calc.add(5,5),10)
        self.assertEqual(Calc.add(5,2),7)
        
        '''or'''
        
    # def test_add(self):
        # result = Calc.add(5,10)
        # result2 = Calc.add(4,2)
        # result3 = Calc.add(4,1)
        # result4 = Calc.add(-4,2)
        # self.assertEqual(result,15)
        # self.assertEqual(result2,6)
        # self.assertEqual(result3,5)
        # self.assertEqual(result4,-2)
        
    def test_sub(self):
        self.assertEqual(Calc.sub(10,5),5)
        self.assertEqual(Calc.sub(11,11),0)
        self.assertEqual(Calc.sub(15,5),10)
        self.assertEqual(Calc.sub(25,2),23)
    
    def test_div(self):
        self.assertEqual(Calc.div(5,2),2.5)    
        
        self.assertRaises(ValueError,Calc.div,2,2)
        
if __name__ == '__main__':
    unittest.main()