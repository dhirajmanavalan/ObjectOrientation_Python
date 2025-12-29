'''Single level inheritance'''
# class Alpha:
#     def fun(self):
#         print("alpha is called..")
        
# class Beta(Alpha):
#     pass

# b = Beta()
# b.fun()

'''Multi level Inheritance'''

# class Alpha:
#     def fun1(self):
#         print("inside alpha")
       
# class Beta(Alpha): 
#     def fun2(self):
#         print('inside beta')
        
# class Gamma(Beta):
#     pass
    
# g = Gamma()
# g.fun1()
# g.fun2()

# print(dir(Gamma))

'''Multiple Inheritance'''

# class Alpha:
#     def fun1(self):
#         print("inside alpha..")
    
# class Beta:
#     def fun2(self):
#         print('inside beta...')
        
# class Gamma(Alpha, Beta):
#     pass

# g = Gamma()
# g.fun1()
# g.fun2()

class Alpha:
    def fun(self):
        print('inside alpha..')
    
class Beta:
    def fun(self):
        print('inside beta')
        
class Gamma(Alpha,Beta):
    def fun(self):
        pass

g = Gamma()
g.fun()
g.fun()

# help(Gamma)