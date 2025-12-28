# def alpha(ref):
#     print("DHira")
#     ref()
    
# def beta():
#     print("Dinesh")
    
# alpha(beta)

# def gsum(lst):
#     s = 0
#     for i in lst:
#         s += i
#     print(s)

# def mul(lst):
#     p = 1
#     for i in lst:
#         p *= i
#     print(p)

# def fun(choice):
#     if choice == 'sum':
#         return gsum
#     else:
#         return mul


# fun1 = fun('sum')
# fun1([10, 20, 30])        # Output: 60

# fun2 = fun('mul')
# fun2([10, 20, 30, 40])    # Output: 240000


# def outer():
#     print('outer')
    
#     def inner():
#         print('inner')
        
#     inner()

# outer()

# def outer(ref):
    
#     def wrapper(a,b):
#         if b==0:
#             print('nooo')
#         else:
#             ref(a,b)
    
#     return wrapper

# @outer
# def div(a,b):
#     print(a/b)
    
# div(10,2)
# div(10,0)

# dhi=outer(div)
# dhi(10,2)
# dhi(10,0)
    
# def fun1():
#     print('inside fun1')

# fun1()
# print(fun1)

# fun2 = fun1
# fun2()
# print('inside fun2')
# print(fun2)
                
# def alpha(ref):
#     print("Alpha")
#     ref()

# def beta():
#     print('beta')
    
# alpha(beta)

# def sum_of(lst):
#     print(sum(lst))
    
# def product_of(lst):
#     p=1
#     for i in lst:
#         p *= i
#     print(p)

# def fun(choice):
#     if choice == 'summm':
#         return sum_of
#     else:
#         return product_of
    
# fun1 = fun('summm')
# fun1([10,20,30,40])

# fun2 = fun('product')
# fun2([10,20,30,40])


# def outer():
#     print("outer function..")
    
#     def inner():
#         print("inner function")
        
#     inner()
    
# outer()

# def outer():
#     print("out")
    
#     def inner():
#         print("inner")
        
#     return inner

# in_ref = outer()
# in_ref()

# def outer(ref):
    
#     def wrapper(lst):
#         if 0 in lst:
#             print('0 is there')
#         else:
#             ref(lst)     
    
#     return wrapper

# @outer   #-->internally it will call this function for outer function
# def product_of(lst):
#     p=1
#     for i in lst:
#         p *= i
#     print(p)
    
# # fun1 = outer(product_of)
# # fun1([1,2,3])
# # fun1([1,9,0])

# def outer(ref):
    
#     def wrapper(a,b):
#         if b == 0:
#             print('noooo')
#         else:
#             ref(a,b)
    
#     return wrapper
            
# @outer
# def div(a,b):
#     print(a/b)

# div(1,5)

# def decorator(num):
    
#     def outer(ref):
    
#         def wrapper(lst):
#             lst =  list(map( lambda x : x**num ,lst))
#             ref(lst)
#         return wrapper
#     return outer

# @decorator(int(input("enter number: ")))
# def power_of(lst):
#     p = 1
#     for i in lst:
#         p *= i
#     print(p)
    
# power_of([1,2,3,4,5])
    
# # fun1 = decorator(3)
# # fun2=fun1(power_of)
# # fun2([1,2,3,4,5])