from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10


    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []


    @staticmethod
    def dvd_capacity(): 
        return MovieWorld.DVD_CAPACITY


    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY


    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)


    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)


    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.customer_id(customer_id)
        dvd = self.dvd_id(dvd_id)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"


    def return_dvd(self, customer_id, dvd_id):
        customer = self.customer_id(customer_id)
        dvd = self.dvd_id(dvd_id)
        
        if not dvd in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
          
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"


    def __repr__(self):
        return "\n".join([
            *[str(c) for c in self.customers],
            *[str(d) for d in self.dvds]
        ])


    def customer_id(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None

                
    def dvd_id(self, dvd_id):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd
        return None