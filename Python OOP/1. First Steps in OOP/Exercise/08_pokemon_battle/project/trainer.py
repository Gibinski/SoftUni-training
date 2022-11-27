from pokemon import Pokemon


class Trainer:
    def __init__(self, name: str, pokemons = []):
        self.name = name
        self.pokemons = pokemons


    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"


    def release_pokemon(self, pokemon_name: str):
        for pokemon in self.pokemons:
            if pokemon_name == pokemon.name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"


    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n" + f"Pokemon count {len(self.pokemons)}\n"
        for pokemon in self.pokemons:
            result += "- " + pokemon.pokemon_details()
        return result


# Test Code

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())