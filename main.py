"""

Inheritance
We've made it to the holy grail of object-oriented programming: inheritance. Non-OOP languages like Go and Rust allow for encapsulation and abstraction features as nearly every language does. Inheritance, on the other hand, tends to be unique to class-based languages like Python, Java, and Ruby.

What Is Inheritance?
Inheritance allows one class, the "child" class, to inherit the properties and methods of another class, the "parent" class.

This powerful language feature helps us avoid writing a lot of the same code twice. It allows us to DRY (don't repeat yourself) up our code.

Syntax
Here Cow is a "child" class that inherits from the "parent" class Animal:

class Animal:
    # parent "Animal" class

class Cow(Animal):
    # child class "Cow" inherits "Animal"

The Cow class can reuse the Animal class's constructor with the super() method, super() allows the child class to call methods and constructors from its parent class, in this case, __init__():

class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

class Cow(Animal):
    def __init__(self, num_udders):
        # call the parent constructor to give the cow some legs
        super().__init__(4)

        # set cow specific properties
        self.num_udders = num_udders

Assignment
In Age of Dragons, all the archers are humans, but not all humans are necessarily archers. All humans have a name, but only archers have a __num_arrows property.

Complete the Archer class. It should inherit the Human class. In its constructor it should call its parent's constructor, then also set its unique __num_arrows property.

"""

class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

