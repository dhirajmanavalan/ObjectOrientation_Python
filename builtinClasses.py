"""I want to store users input in list"""


class demo:

    members = []

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

        demo.members.append(self)

    def display(self):
        print(self.__dict__)


class main:
    d = demo("dhiraj", 12, "male")
    d1 = demo("dinesh", 24, "male")
    print(demo.members)
    for i in demo.members:
        i.display()


if __name__ == "__main__":
    main()
