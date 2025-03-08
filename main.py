"""

Dragons
In "Age of Dragons", there are Orcs, Humans, Goblins, Dragons, etc. All of those different creatures are called "units". At the moment, the only thing specific to a unit is that it has a position on the game map and a name.

Dragons, a specific type of unit, can breathe fire in a large area dealing damage to any units that are touched by its fiery blaze.

The Game Grid
Our game map is just a Cartesian plane.

cartesian

Assignment
Complete the unit's in_area method and the dragon's breathe_fire method.

in_area
This method has four parameters, x_1, y_1, x_2, and y_2. The coordinates x_1 and y_1 represent the bottom-left corner of the rectangle, while x_2 and y_2 represent the top-right corner.

To determine if a unit is within or on the boundary of this rectangle, use the unit's position coordinates pos_x and pos_y. If the unit's position falls inside or on the edge of the rectangle, the method returns True. Otherwise, it returns False.

breathe_fire
This method causes the dragon to breathe a swath of fire in the target area. The target area is centered at (x,y). The area stretches for __fire_range in both directions inclusively.

For each unit in the units list, append that unit to a list if the unit is within the blast. Return the list of units hit by the blast.

Example of Fire Breath Hitting a Unit
breath hitting unit

The example above uses a __fire_range of 1 centered at (1, 1).

"""

class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        x_true = False
        y_true = False

        for num in range(x_1, x_2+1):
            if self.pos_x == num:
                x_true = True
                break

        for num in range(y_1, y_2+1):
            if self.pos_y == num:
                y_true = True
                break
        return True if x_true and y_true else False



class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        affected_units = []

        effective_x_cords = [_ for _ in range(x, x+self.__fire_range+1)] + ([_ for _ in range(x-1, x-self.__fire_range-1, -1)])
        effective_y_cords = [_ for _ in range(y, y+self.__fire_range+1)] + ([_ for _ in range(y-1, y-self.__fire_range-1, -1)])

        for unit in units:
            if unit.pos_x in effective_x_cords and unit.pos_y in effective_y_cords:
                affected_units.append(unit)
        return affected_units

