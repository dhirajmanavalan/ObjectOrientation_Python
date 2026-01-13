
# from main import check_weather

# from main import add,divide
# import pytest

# def test_check_weather():
#     assert check_weather(20) == "Hot"
#     assert check_weather(10) == "Cold"
#     assert check_weather(110) == "Hot"


'''Another example'''

# def test_add():
#     assert add(2,3) == 5
#     assert add(1,-1) == 0
#     assert add(0,0) == 0
    
# def test_divide():
#     with pytest.raises(ValueError,match="Zero is not divide"):
#         divide(2,0) == 0
    
    
'''Another example'''
# import pytest
# from main import UserManager 

# @pytest.fixture
# def user_manager():
#     return UserManager()

# # user_manager = UserManager()

# def test_add_user(user_manager):
#     assert user_manager.add_user("dhiru","dhiru@gmail.com") == True
#     assert user_manager.get_user("dhiru") == "dhiru@gmail.com"
    
# def test_duplicate_user(user_manager):
#     user_manager.add_user("dhiru","dhiru@gmail.com")
#     with pytest.raises(ValueError):
#         user_manager.add_user("dhiru","dhiru@gmail.com")
    
'''another example'''

from main import is_prime

import pytest

@pytest.mark.parametrize("num1 , result", [
    
    (2,True),
    (1,False),
    (3,False),
    (4,False),
    (5,True),
    
])

def test_is_prime(num1,result):
    assert is_prime(num1) == result