class Car:
    def __init__(self):
        self.brand = "BMW"
    
    def car_engine(self):
        print("Hello")
    
def main():
    c = Car()
    print(c.brand)
    c.car_engine()

    c2 = Car()
    c2.car_engine()
    print(c2.brand)

if __name__ == '__main__':
    main