import random


class Character:
    def __init__(self):
        # sets the sum of the three highest values in four dice rolls to each ability
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        # floors the number of the modifier by making an exact division
        self.hitpoints = 10 + int(((self.constitution - 10) / 2) // 1)

    def ability(self):
        rolls = []
        for i in range(4):
            rolls.append(random.randint(1, 6))
        return sum(sorted(rolls, reverse=True)[:3])


def modifier(constitution):
    return int(((constitution - 10) / 2) // 1)
