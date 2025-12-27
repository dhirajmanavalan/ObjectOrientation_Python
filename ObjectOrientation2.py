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

def main():
    cr = Football('christiano','Juventus',746)
    print(cr.name)
    print(cr.team)
    print(cr.goals)
    cr.shooting()
    cr.passing()
    cr.running()

if __name__ == '__main__':
    main()
