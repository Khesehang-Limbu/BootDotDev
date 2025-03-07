"""

Archers
Assignment
Complete the Archer class.

Constructor
The constructor should take the following parameters in order and set them as properties:

name
health
num_arrows
get_shot method
Complete the get_shot method. It operates on the current archer instance.

If the current archer has health left, remove one health from the current archer. Then, if the archer's health is 0, raise the exception: {} is dead where {} is the archer's name.

shoot method
Finish the shoot method. It takes an Archer instance as the target input.

If the shooter has no arrows left, raise the exception {} can't shoot where {} is the shooter's name. Otherwise, remove an arrow from the shooter and print {1} shoots {2} where {1} is the shooter's name and {2} is the name of the targeted archer. Next, call the target's get_shot() method.

"""

class Archer:
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def get_shot(self):
        self.health -= 1

        if self.health == 0:
            raise Exception(f"{self.name} is dead")

    def shoot(self, target):
        if self.num_arrows == 0:
            raise Exception(f"{self.name} can't shoot")

        self.num_arrows -= 1
        print(f"{self.name} shoots {target.name}")
        target.get_shot()


    # don't touch below this line

    def get_status(self):
        return self.name, self.health, self.num_arrows

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")

