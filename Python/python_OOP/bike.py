class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print('Miles =',self.miles, ', max speed = ', self.max_speed, ', price = ', self.price)
        return self
    def ride(self):
        self.miles += 10
        print('Riding')
        return self
    def reverse(self):
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        print('Reversing')
        return self


 
bike1 = Bike(200, "25mph" )
bike2 = Bike(300, "35mph" )
bike3 = Bike(400, "45mph" )

print('############### bike 1')
bike1.ride().ride().ride().reverse().displayInfo()
print('############### bike 2')
bike2.ride().ride().reverse().reverse().displayInfo()
print('############### bike 3')
bike3.reverse().reverse().reverse().displayInfo()
