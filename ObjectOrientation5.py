# '''instance method execution'''
# class BMW:
#     def __init__(self,name,cc,color):
#         self.name = name
#         self.cc = cc
#         self.color = color

#     def car_parts(self):
#         print(self.name, "car parts these..")

#     def simple(self):
#         print(self.name)
#         print(self.cc)
#         print(self.color)


# def main():
#         b = BMW('a',120,'blue')
#         b.simple()

# if __name__ == '__main__':
#     main()

# '''Static method execution --> i can call using class and object alsoo.. **without using object creation**'''
# class BMW:
#     def __init__(self,name,cc,color):
#         self.name = name
#         self.cc = cc
#         self.color = color

#     def car_parts(self):
#         print(self.name, "car parts these..")

#     @staticmethod
#     def kms_mile(kms):
#         print(kms * 1.6)

#     def simple(self):
#         print(self.name)
#         print(self.cc)
#         print(self.color)


# def main():
#         b = BMW('a',120,'blue')
#         b.simple()
#         BMW.kms_mile(2)
#         b.kms_mile(2)

# if __name__ == '__main__':
#     main()

"""class method execution --> by using class creating an object"""


class BMW:
    def __init__(self, name, cc, color):
        self.name = name
        self.cc = cc
        self.color = color

    @classmethod
    def x1(cls):
        return cls("x1", 250, "black")

    @classmethod
    def x2(cls):
        return cls("x2", 450, "blue")

    def display(self):
        print(self.name)
        print(self.cc)
        print(self.color)


def main():
    fun1 = BMW.x1()
    fun2 = BMW.x2()

    fun1.display()
    fun2.display()


if __name__ == "__main__":
    main()
