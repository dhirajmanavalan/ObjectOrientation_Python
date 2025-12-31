"""This is logger for im taking an examplee inside print statements looks like clumsy soo im using loggers to overcome"""

# def sum_even(lst):
#     print("sum_even() started excution")
#     sum = 0
#     for i in lst:
#         if i % 2 == 0:
#             sum = sum + i

#     print("sum_even() finished excution")
#     return sum


# def main():
#     print("main() started excution")

#     lst = list(map(int, input().split()))
#     print("input taken from user")
#     print("calling sum_even()")
#     res = sum_even(lst)
#     print("print result of sum_even() collected")
#     print(res)
#     print("main() finished excution")


# main()

"""Using log file to achieve this program"""

import logging


def sum_even(lst):
    logging.info("sum_even() started excution")
    sum = 0
    for i in lst:
        if i % 2 == 0:
            sum = sum + i

    logging.info("sum_even() finished excution")
    return sum


def main():
    logging.basicConfig(filename="log.txt", level=logging.INFO)
    logging.info("main() started excution")

    lst = list(map(int, input().split()))
    logging.info("input taken from user")
    logging.info("calling sum_even()")
    res = sum_even(lst)
    logging.info("print result of sum_even() collected")
    print(res)
    logging.info("main() finished excution")


main()
