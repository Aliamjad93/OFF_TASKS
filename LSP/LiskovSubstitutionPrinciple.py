# Defining a base class called 'Bird'
class Bird:
    # A method within the Bird class, representing the action of flying
    def fly(self):
        pass

# Defining a derived class 'Sparrow' which inherits from the 'Bird' class
class Sparrow(Bird):
    # Overriding the 'fly' method from the base class to provide the specific behavior for Sparrows
    def fly(self):
        print("Sparrow can fly")

# Defining another derived class 'Penguin' which inherits from the 'Bird' class
class Penguin(Bird):
    # Overriding the 'fly' method to provide a different behavior for Penguins
    def fly(self):
        print("Penguin cannot fly")

# A function that takes a 'bird' object as a parameter and invokes its 'fly' method
def make_bird_fly(bird):
    bird.fly()

# Main program
# Creating an instance of the 'Sparrow' class
sparrow = Sparrow()
# Creating an instance of the 'Penguin' class
penguin = Penguin()

# Calling the 'make_bird_fly' function with a Sparrow object
# The 'fly' method of the Sparrow class is executed, and "Sparrow can fly" is printed
make_bird_fly(sparrow)  # Outputs: "Sparrow can fly"

# Calling the 'make_bird_fly' function with a Penguin object
# The 'fly' method of the Penguin class is executed, and "Penguin cannot fly" is printed
make_bird_fly(penguin)  # Outputs: "Penguin cannot fly"
