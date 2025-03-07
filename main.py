"""

Encapsulation
Encapsulation is the practice of hiding complexity inside a "black box" so that it's easier to focus on the problem at hand.

encapsulation

The most basic example of encapsulation is a function. The caller of a function doesn't need to worry too much about what happens inside, they just need to understand the inputs and outputs.

acceleration = calc_acceleration(initial_speed, final_speed, time)

To use the calc_acceleration function, we don't need to think about every individual line of code inside the function. We just need to know that if we give it the inputs:

initial_speed
final_speed
time
Then it will give us the correct acceleration as an output.

Public and Private
By default, all properties and methods in a class are public. That means that you can access them with the . operator:

wall.height = 10
print(wall.height)
# 10

Private data members are how we encapsulate logic and data within a class. To make a property or method private, you just need to prefix it with two underscores.

class Wall:
    def __init__(self, armor, magic_resistance):
        self.__armor = armor
        self.__magic_resistance = magic_resistance

    def get_defense(self):
        return self.__armor + self.__magic_resistance

front_wall = Wall(10, 20)

# This results in an error
print(front_wall.__armor)

# This works
print(front_wall.get_defense())
# 30

We do this because, in this example, armor and magic_resistance are implementation details. After creating a Wall, they don't matter anymore. Now the game developers can just call get_defense and not worry about how it's calculated under the hood.

Assignment
Complete the Wizard class's constructor. It should set 2 private properties:

"stamina"
"intelligence"
Don't forget to make them private! Use the values passed into the constructor to set the properties.

It should also set 3 public properties:

name: Use the value passed into the constructor.
health: 100x the value of "stamina".
mana: 10x the value of "intelligence".

"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for b in self.books:
            if b.title == book.title and b.author == book.author:
                self.books.remove(b)

    def search_books(self, search_string):
        searched_books = []
        for book in self.books:
            if search_string.lower() in book.title.lower() or search_string.lower() in book.author.lower():
                searched_books.append(book)
        return searched_books
