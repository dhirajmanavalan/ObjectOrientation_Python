import logging

logging.basicConfig(filename="log.txt", level=logging.ERROR)


def div():
    num = int(input("Enter the numberator: "))
    den = int(input("Enter the denominator: "))
    print(f"Enter the Numerator: {num}")
    print(f"Enter the Denominator: {den}")

    try:
        q = num / den
        print(q)
    except:
        logging.error("division is error")


div()
