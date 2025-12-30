"""without object orientation"""

# from math import pi

# class Circle:
#     def __init__(self):
#         self.r = 0
#         self.area = 0

#     def input(self):
#         self.r = int(input("Enter the radius:"))

#     def find_area(self):
#         self.area = pi * self.r**2

#     def disp_area(self):
#         print(self.area)

# class Rectangle:
#     def __init__(self):
#         self.l = 0
#         self.b = 0
#         self.area = 0

#     def input(self):
#         self.l = int(input("Enter leangth"))
#         self.b = int(input("Enter breadth"))


#     def find_area(self):
#         self.area = self.l * self.b

#     def display(self):
#         print(self.area)

# class Triangle:
#     def __init__(self):
#         self.h = 0
#         self.b = 0
#         self.area = 0

#     def input(self):
#         self.h = int(input("Enter height"))
#         self.b = int(input("Enter base  "))


#     def find_area(self):
#         self.area = (self.h * self.b)/2

#     def display(self):
#         print(self.area)


# def main():
#     c = Circle()
#     r = Rectangle()
#     t = Triangle()

#     c.input()
#     c.find_area()
#     c.disp_area()

#     r.input()
#     r.find_area()
#     r.display()

#     t.input()
#     t.find_area()
#     t.display()

# main()


"""Using object orientation"""

from math import pi

from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self):
        self.area = 0

    @abstractmethod
    def input(self):
        pass

    @abstractmethod
    def find_area(self):
        pass

    @abstractmethod
    def display(self):
        pass


class Circle(Shape):
    def __init__(self):
        self.r = 0
        super().__init__()

    def input(self):
        self.r = int(input("Enter the radius:"))

    def find_area(self):
        self.area = pi * self.r**2

    def display(self):
        print(f"Circle area = {self.area}")


class Rectangle(Shape):
    def __init__(self):
        self.l = 0
        self.b = 0
        super().__init__()

    def input(self):
        self.l = int(input("Enter leangth"))
        self.b = int(input("Enter breadth"))

    def find_area(self):
        self.area = self.l * self.b

    def display(self):
        print(f"Rectangle area = {self.area}")


class Triangle(Shape):
    def __init__(self):
        self.h = 0
        self.b = 0
        super().__init__()

    def input(self):
        self.h = int(input("Enter height"))
        self.b = int(input("Enter base  "))

    def find_area(self):
        self.area = (self.h * self.b) / 2

    def display(self):
        print(f"Triangle area = {self.area}")


def geometric_shape(dhi):
    dhi.input()
    dhi.find_area()
    dhi.display()


def main():
    c = Circle()
    r = Rectangle()
    t = Triangle()

    geometric_shape(c)
    geometric_shape(r)
    geometric_shape(t)


main()
