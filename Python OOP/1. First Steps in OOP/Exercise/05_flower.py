class Flower:

    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False


    def water(self, quantity):
        if self.water_requirements <= quantity:
            self.is_happy = True


    def status(self):
        y = "not "
        if self.is_happy:
            y = ""

        return f"{self.name} is {y}happy"


#test Code
flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())