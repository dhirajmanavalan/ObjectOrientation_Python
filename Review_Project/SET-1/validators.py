import re

class InvalidEmailError(Exception):
    pass

class InvalidPhoneError(Exception):
    pass

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise InvalidEmailError(f"Invalid email: {email}")

def validate_phone(phone):
    pattern = r'^[6-9]\d{9}$'
    if not re.match(pattern, phone):
        raise InvalidPhoneError(f"Invalid phone number: {phone}")
