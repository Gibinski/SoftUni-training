from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):
    IMCREASE = 0.1

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food not in self.food_that_eats:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * IMCREASE


class Dog(Mammal):
    IMCREASE = 0.4

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def food_that_eats(self):
        return [Meat]

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    IMCREASE = 0.3

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)


    @property
    def food_that_eats(self):
        return [Vegetable, Meat]

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    IMCREASE = 1.0

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def food_that_eats(self):
        return [Meat]

    def make_sound(self):
        return "ROAR!!!"
