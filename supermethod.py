"""example 1"""

# class Customer:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

# class PlatinumCustomers(Customer):
#     def __init__(self, name, age, gender,platinum_id):
#         super().__init__(name,age,gender)
#         self.platinum_id = platinum_id

#     def display(self):
#         print(self.__dict__)

# def main():
#     pc = PlatinumCustomers('dhiraj',12,'male',10)
#     pc.display()

# if __name__ == '__main__':
#     main()

"""example 2"""
# class Customer:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def place_order(self,dish):
#         cost = 0
#         del_charge = 50
#         if dish == 'pizza':
#             cost = 500  + del_charge
#         else:
#             cost = 250 + del_charge

#         return cost

# class plat_customer(Customer):
#     def __init__(self,name,age,gender,plat_id):
#         super().__init__(name,age,gender)
#         self.plat_id = plat_id

#     def place_order(self,dish):
#         del_charge = 50
#         return (super().place_order(dish) - del_charge)*0.95

# class main():
#    pc =  plat_customer('dhria',12,'male',10)
#    print(pc.place_order('pizza'))

# if __name__ == '__main__':
#     main()

"""super method using in multilevel inheritance"""
# class alpha:
#     def fun(self):
#         print('A')

# class beta(alpha):
#     def fun(self):
#         print('B')

# class Gamma(beta):
#     def fun(self):
#         super(beta,self).fun()
#         super().fun()
#         print('C')

# g = Gamma()
# g.fun()

"""super method using in multiple inheritance"""


class A:
    def fun(self):
        print("A")


class B:
    def fun(Self):
        print("b")


class C(A, B):
    def fun(self):
        super().fun()
        print("c")


dhi = C()
dhi.fun()
