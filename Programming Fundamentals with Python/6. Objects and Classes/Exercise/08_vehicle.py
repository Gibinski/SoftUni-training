class Vehicle:

    def __init__(self, type, model, price, owner = None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner


    def buy(self, money: int, owner: str):
        result = ""
        if self.price <= money and self.owner == None:
            self.owner = owner
            change = money - self.price
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
        
        if self.price > money: 
            result = "Sorry, not enough money"

        if self.price > money and self.owner != None:
            result += "\n"

        if self.owner != None:
            result += "Car already sold"
        return result


    def sell(self):
        if self.owner == None:
            return "Vehicle has no owner"
        else:
            self.owner = None


    def __repr__(self):
        if self.owner == None:
            return F"{self.model} {self.type} is on sale: {self.price}"
        else:
            return f"{self.model} {self.type} is owned by: {self.owner}"

vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)