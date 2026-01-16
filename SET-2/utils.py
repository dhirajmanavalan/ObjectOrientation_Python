import re

class InvalidEmployeeCodeError(Exception):
    pass


def format_name(name: str) -> str:
    # Capitalize each word
    return name.strip().title()


def validate_employee_code(code: str) -> bool:
    # Format: EMP123
    pattern = r"^EMP\d{3}$"
    if not re.match(pattern, code):
        raise InvalidEmployeeCodeError(f"Invalid employee code: {code}")
    return True
