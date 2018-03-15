class Car(object):
    def __init__(self, price, speed, fuel, milage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        self.tax = 0.12
        if self.price>100000:
            self.tax = 0.15
    def display_all(self):
        print('Price: '+ str(self.price))
        print('Speed: '+ str(self.speed)+'mph')
        print('Fuel: '+ str(self.fuel))
        print('Milage: '+ str(self.milage)+'mpg')
        print('Tax: '+ str(self.tax))
        return self
  

car1 = Car(2000, 35, "Full" , 15)
car2 = Car(2000, 5, "Not Full" , 105)
car3 = Car(2000, 35, "Full" , 15)
car4 = Car(2000, 35, "Empty" , 15)
car5 = Car(2000, 35, "Full" , 15)
car6 = Car(200000, 35, "Full" , 15)

for i in range(1,6):
    vars()['car' + str(i)].display_all()

