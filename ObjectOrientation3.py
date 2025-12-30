class Citizen:

    nationality = "Indian"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def simple(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.nationality)


def main():
    dhiraj = Citizen("Dhiraj", 23, "M")
    dinesh = Citizen("DInesh", 23, "M")
    monisha = Citizen("Monisha", 30, "F")
    dhiraj.simple()
    dinesh.simple()
    monisha.simple()


if __name__ == "__main__":
    main()
