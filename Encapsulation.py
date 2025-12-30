"""
--> for private keyword use *_bal* --> this is convention we want to follow for python developers
"""

# class AccountHolder:

#     def __init__(self):
#         self._bal = 10000

#     def get_bal(self):
#         return self._bal

#     def set_bal(self,amt):
#         if amt > 0 :
#             self._bal = amt
#         else:
#             print('Invalid amount')

# ah = AccountHolder()
# ah.set_bal(20000)
# print(ah.get_bal())

"""
By using data Mangling we can achieve private keyword..
data managling achieve -- when we use it it will CHANGE private variable name has ** __VARIABLENAME --> _classname __ variable name**
"""

# class AccountHolder:

#     def __init__(self):
#         self.__bal = 10000

#     def get_bal(self):
#         return self.__bal

#     def set_bal(self,amt):
#         if amt > 0 :
#             self.__bal = amt
#         else:
#             print('Invalid amount')

# ah = AccountHolder()
# ah.set_bal(20000)
# print(ah.get_bal())


"""Encapsulation"""

# class AccountHolder:
#     def __init__(self):
#         self.__balance = int(input("Enter balance amount: "))

#     def get_balance(self):
#         return self.__balance

#     def set_balance(self,amount):
#         self.__balance=amount

#     balance1 = property(get_balance,set_balance)

# ah = AccountHolder()
# ah.balance1=1200
# print(ah.balance1)


# class AccountHolder:
#     def __init__(self):
#         self.__balance = int(input("Enter balance amount: "))

#     @property
#     def bala(self):
#         return self.__balance

#     @bala.setter
#     def bala(self,amount):
#         self.__balance=amount

#     # balance1 = property(get_balance,set_balance)

# ah = AccountHolder()
# ah.bala = 1222
# print(ah.bala)


class AccountHolder:
    def __init__(self):
        self.__balance = 12000

    @property
    def bal(self):
        return self.__balance

    @bal.setter
    def bal(self, amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("invalid amount..")


ah = AccountHolder()
ah.bal = -20000
print(ah.bal)
