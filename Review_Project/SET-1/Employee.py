from validators import validate_email, validate_phone

class Employee:
    def __init__(self, emp_id, name, email, phone):
        self.emp_id = emp_id
        self.name = name
        self.email = email
        self.phone = phone
        self.validate()

    def validate(self):
        validate_email(self.email)
        validate_phone(self.phone)
