"""

Sprint
In the game we're making, Age of Dragons, humans can "sprint" allowing them to move twice as fast. However, sprinting requires __stamina. Each time a human sprints, it loses stamina. Once it is out of stamina, it can no longer sprint.

Assignment
Complete all of the missing methods.

The __raise_if_cannot_sprint() and __use_sprint_stamina() are private methods that are only intended to be used within the class. In your case, you'll use them to build the other four sprinting methods.

__raise_if_cannot_sprint()
This method should raise the exception: not enough stamina to sprint if the human is out of stamina.

__use_sprint_stamina()
Remove one stamina from the human.

For Each of the Remaining Methods:
Raise an error if there isn't enough stamina to sprint (use __raise_if_cannot_sprint()).
Use the stamina needed to sprint (use __use_sprint_stamina())
Move twice in the direction of the sprint.

"""

class Human:
    def sprint_right(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.__pos_x += 2 * self.__speed

    def sprint_left(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.__pos_x -= 2 * self.__speed

    def sprint_up(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.__pos_y += 2 * self.__speed

    def sprint_down(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        self.__pos_y -= 2 * self.__speed

    def __raise_if_cannot_sprint(self):
        if self.__stamina == 0:
            raise Exception("not enough stamina to sprint")

    def __use_sprint_stamina(self):
        self.__stamina -= 1

    # don't touch below this line

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x, pos_y, speed, stamina):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina

