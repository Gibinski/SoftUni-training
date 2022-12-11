from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, age: int, gender: str):
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self):
        ...

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"
  
