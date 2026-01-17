import unittest
from employee import Employee
from report import EmployeeReport

class TestEmployeeReport(unittest.TestCase):

    def test_grade_A(self):
        emp = Employee("EMP01", "Alex", 60000, 95)
        report = EmployeeReport(emp)
        self.assertEqual(report.generate_grade(), "A")

    def test_grade_B(self):
        emp = Employee("EMP002", "Bob", 35000, 85)
        report = EmployeeReport(emp)
        self.assertEqual(report.generate_grade(), "B")

    def test_grade_C(self):
        emp = Employee("EMP3", "Carol", 22000, 72)
        report = EmployeeReport(emp)
        self.assertEqual(report.generate_grade(), "C")

    def test_grade_D(self):
        emp = Employee("EMP004", "Dan", 15000, 60)
        report = EmployeeReport(emp)
        self.assertEqual(report.generate_grade(), "D")


if __name__ == "__main__":
    unittest.main()
