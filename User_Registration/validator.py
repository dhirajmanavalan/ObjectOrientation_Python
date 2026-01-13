import re

def vaildate_email(email):
    regex =  r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(regex,email))

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[@$!%*?&]', password):
        return False
    return True
        
    