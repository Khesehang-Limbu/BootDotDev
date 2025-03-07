"""

Wizard Duel
Let's give our wizards the ability to launch fireballs at each other.

Assignment
Complete the cast_fireball and is_alive methods.

cast_fireball
If there isn't enough mana to cast a fireball (see fireball_cost at the top of the file), raise an Exception with the message ____ cannot cast fireball, where ____ is the wizard's name.

If the wizard has enough mana, reduce their mana by the fireball_cost and make sure to call get_fireballed on the target wizard or they'll be stuck in an endless battle.

is_alive
This method should return True if the wizard's health is greater than 0, and False otherwise.

"""

fireball_damage = 500
potion_mana = 100
fireball_cost = 50


class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def cast_fireball(self, target):
        if self.mana < fireball_cost:
            raise Exception(f"{self.name} cannot cast fireball")
        self.mana -= fireball_cost
        target.get_fireballed()

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def get_fireballed(self):
        self.health -= 500

    def drink_mana_potion(self):
        self.mana += 100
