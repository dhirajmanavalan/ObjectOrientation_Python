from employee import Employee
from report import EmployeeReport
from utils import InvalidEmployeeCodeError

try:
    emp = Employee(
        emp_code="EMP101",
        name="dhiraj kumar",
        salary=52000,
        attendance=92
    )

    report = EmployeeReport(emp)
    report.save_report()

    print("Employee report generated successfully")

except InvalidEmployeeCodeError as e:
    print(e)
