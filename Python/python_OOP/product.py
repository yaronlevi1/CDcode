class Product(object):
    def __init__(self, price, itemName, weight, brand):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def addTax(self, rate):
        self.price *= (1+rate)
        return self
    def Return(self, reason):
        self.reason = reason
        if self.reason == "defective":
            self.status = "defective"
            self.price = 0
        if self.reason == "box":
            self.status = "for sale"
        if self.reason == "opened":
            self.status = "used"
            self.price *= 0.8
        return self
    def displayInfo(self):
        print('Price: '+ str(self.price))
        print('Item Name: '+ str(self.itemName))
        print('Weight: '+ str(self.weight))
        print('Brand: '+ str(self.brand))
        print('Status: '+ str(self.status))
        return self


p1 = Product( 200, "shoes", 2, "NB")
p1.displayInfo()
p1.sell().displayInfo()
p1.addTax(0.15).displayInfo()

