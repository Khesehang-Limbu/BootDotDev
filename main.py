"""

Wizard Duel
Let's have ourselves a Wizard's duel.

Assignment
Add the following methods to the Wizard class.

get_fireballed()
This method operates on the instance of the class. It takes no inputs and returns no values explicitly, but it should remove 500 health from the wizard.

drink_mana_potion()
This method operates on the instance of the class. It takes no inputs and returns no values explicitly, but it should add 100 mana to the wizard's reserves.

"""

fireball_damage = 500
potion_mana = 100


class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def get_fireballed(self):
        self.health -= 500

    def drink_mana_potion(self):
        self.mana += 100
