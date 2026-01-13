# def check_weather(temp):
#     if temp >= 20:
#         return "Hot"
#     elif temp < 20:
#         return "Cold"

'''Another example'''

# def add(a,b):
#     return a+b

# def divide(a,b):
#     if b ==0:
#         raise ValueError("Zero is not divide")
#     else:
#         return a/b

'''Another example'''

# class UserManager:
#     def __init__(self):
#         self.users = {}
        
#     def add_user(self,username,email):
#         if username in self.users:
#             raise ValueError("User already exists")
#         self.users[username]=email
#         return True
    
#     def get_user(self,username):
#         return self.users.get(username)

'''Another example'''

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True