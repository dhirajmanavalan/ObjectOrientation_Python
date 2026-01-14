import unittest
from employee import Employee

class test_employee(unittest.TestCase):
    
    def setUp(self):
        self.emp_1 = Employee('dhiraj','kumar',2000)
        self.emp_2 = Employee('dinesh','kumar',4000)
        
    
    def test_email(self):
          
        self.assertEqual(self.emp_1.email, 'dhiraj.kumar@email.com')
        self.assertEqual(self.emp_2.email, 'dinesh.kumar@email.com')
        
        self.emp_1.first = 'dhiraj'
        self.emp_2.first = 'dinesh'
        
        self.assertEqual(self.emp_1.email, 'dhiraj.kumar@email.com')
        self.assertEqual(self.emp_2.email, 'dinesh.kumar@email.com')
        
    def test_fullname(self):
        
        self.assertEqual(self.emp_1.fullname, 'dhirajkumar')
        self.assertEqual(self.emp_2.fullname, 'dineshkumar')
        
        self.emp_1.first = 'dhiraj'
        self.emp_2.first = 'dinesh'
        
        self.assertEqual(self.emp_1.fullname, 'dhirajkumar')
        self.assertEqual(self.emp_2.fullname, 'dineshkumar')
        
    def test_apply_pay(self):
             
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 2100)
        self.assertEqual(self.emp_2.pay,4200)
        
if __name__ == '__main__':
    unittest.main()