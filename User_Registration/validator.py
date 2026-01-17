
from validator import InvalidEmailError, InvalidPhoneError

try:
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    emp = Employee(emp_id, name, email, phone)
    print("Employee created successfully")

except ValueError:
    print("Employee ID must be a number")
except (InvalidEmailError, InvalidPhoneError) as e:
    print(e)
