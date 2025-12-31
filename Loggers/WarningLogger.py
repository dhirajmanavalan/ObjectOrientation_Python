import logging


def validate(num):
    if len(num) == 10:
        print("validate mobile number..")
    else:
        logging.warning("Mobile number validation failed")
        print("Invalid mobile number..")


def main():
    logging.basicConfig(filename="log.txt", level=logging.WARNING)

    num = input("Enter mobile number: \n")
    validate(num)


main()
