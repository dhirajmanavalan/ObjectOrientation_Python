class EmployeeReport:
    def __init__(self, employee):
        self.employee = employee

    def generate_grade(self):
        salary = self.employee.salary
        attendance = self.employee.attendance

        if salary >= 50000 and attendance >= 90:
            return "A"
        elif salary >= 30000 and attendance >= 80:
            return "B"
        elif salary >= 20000 and attendance >= 70:
            return "C"
        else:
            return "D"

    def save_report(self):
        grade = self.generate_grade()
        with open("employee_report.txt", "a") as file:
            file.write(
                f"Code: {self.employee.emp_code}, "
                f"Name: {self.employee.name}, "
                f"Salary: {self.employee.salary}, "
                f"Attendance: {self.employee.attendance}%, "
                f"Grade: {grade}\n"
            )
