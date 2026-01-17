from utils import format_name, validate_employee_code

class Employee:
    def __init__(self, emp_code, name, salary, attendance):
        validate_employee_code(emp_code)
        self.emp_code = emp_code
        self.name = format_name(name)
        self.salary = salary
        self.attendance = attendance
