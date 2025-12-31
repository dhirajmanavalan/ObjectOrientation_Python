# import logging

# def add(x,y):
#     return x+y

# def sub(x,y):
#     return x-y

# def mul(x,y):
#     return x*y

# def div(x,y):
#     return x/y

# def main():

#     a = 10
#     b = 5
#     print(f'a = {a}')
#     print(f'b = {b}')

#     res1= add(a,b)
#     print(f'res1 = {res1}')
#     res2= sub(a,b)
#     print(f'res2 = {res2}')
#     res3= mul(a,b)
#     print(f'res3 = {res3}')
#     res4= div(a,b)
#     print(f'res4 = {res4}')

# main()


import logging


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def main():
    logging.basicConfig(filename="log.txt", level=logging.DEBUG)

    a = int(input())
    b = int(input())
    logging.debug(f"a = {a}")
    logging.debug(f"b = {b}")

    res1 = add(a, b)
    logging.debug(f"res1 = {res1}")
    res2 = sub(a, b)
    logging.debug(f"res2 = {res2}")
    res3 = mul(a, b)
    logging.debug(f"res3 = {res3}")
    res4 = div(a, b)
    logging.debug(f"res4 = {res4}")


main()
