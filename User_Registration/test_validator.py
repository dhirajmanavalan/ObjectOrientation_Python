from validator import vaildate_email,validate_password
import pytest

@pytest.mark.parametrize("email, expected",[
    ("test@gmail.com", True),
    ("user.name@yahoo.com", True),
    ("user@domain.co.in", True),
    ("invalid@", False),
    ("@gmail.com", False),
    ("testgmail.com", False),
])

def test_validate_email(email,expected):
    assert vaildate_email(email) == expected
    
    
@pytest.mark.parametrize("password, expected", [
    ("Abc@1234", True),
    ("Strong@1", True),
    ("abc123", False),
    ("ABC12345", False),
    ("Abcdefgh", False),
    ("Abc@12", False),
])

def test_validate_password(password, expected):
    assert validate_password(password) == expected   