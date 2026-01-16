from Employee import Employee
from validators import InvalidEmailError, InvalidPhoneError

try:
    emp = Employee(
        emp_id=101,
        name="Dhiraj",
        email="dhiraj@gmail.com",
        phone="9876543210"
    )
    print("Employee created successfully")

except (InvalidEmailError, InvalidPhoneError) as e:
    print(e)
