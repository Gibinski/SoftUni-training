class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"


    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cost

        return f"Skill {skill_name} added to the collection of the player {self.name}"


    def player_info(self):
        result = [f"Name: {self.name}"]
        result.append(f"Guild: {self.guild}")
        result.append(f"HP: {self.hp}")
        result.append(f"MP: {self.mp}")

        for name, cost in self.skills.items():
            result.append(f"==={name} - {cost}")

        return "\n".join(result)


# Test Code

# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())