class Football:
    def __init__(self,name,team,goals):
        self.name = name
        self.team = team
        self.goals = goals
    def shooting(self):
        print(self.name, "is shooting")
    
    def passing(self):
        print(self.name, "is passing")

    def running(self):
        print(self.name, "is running")

    def simple(self):
        print(self.name)
        print(self.team)
        print(self.goals)
        print(self.age)



def main():
    cr = Football('christiano','Juventus',746)
    cr.age = 12
    cr.simple()
    cr.shooting()
    cr.passing()
    cr.running()

    

    rd = Football('Ronaldo','Tirupathur','400')
    rd.age=25
    
    setattr(rd,'age',12)
    print(getattr(rd,'age'))
    print(hasattr(rd,'ee'))
    rd.simple()
    rd.shooting()
    rd.passing()
    rd.running()

if __name__ == '__main__':
    main()
