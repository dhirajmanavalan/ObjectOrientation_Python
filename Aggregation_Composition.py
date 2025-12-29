class Food_Item:
    def __init__(self,name,quantity,veg):
        self.name = name
        self.quantity = quantity
        self.veg = veg
        
class Delivery_Agent:
    def __init__(self,name,rating,ph_no):
        self.name = name
        self.rating = rating
        self.ph_no = ph_no
        
class Restaurant:
    def __init__(self,name,addr,rating):
        self.name = name
        self.addr = addr
        self.rating = rating
        self.Food_Item =Food_Item('Pizza',1,True)
        
    def assign_delivery_agent(self,agent):
        self.agent = agent
        
def main():
    r =   Restaurant('lakshmi cafe','tirupathur',4.5)
    dhiraj = Delivery_Agent('dhiraj',4.9,8489403967)
    r.assign_delivery_agent(dhiraj)
    print(r.agent)
    
if __name__ == '__main__':
    main()