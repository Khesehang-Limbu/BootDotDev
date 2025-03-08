"""

Rectangles
You discovered that to properly calculate army formations in the game, you needed to be able to get the area and perimeter of squares and rectangles of various sizes.

Challenge
Finish implementing the empty methods of the Rectangle and Square classes. All squares are rectangles, but not all rectangles are squares.

Note: Due to inheritance of methods, the Square class should only need to implement the __init__ method.

"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2*(self.length + self.width)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
