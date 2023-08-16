class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

def make_bird_fly(bird):
    bird.fly()

# Main program
sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)  # Outputs: "Sparrow can fly"
make_bird_fly(penguin)  # Outputs: "Penguin cannot fly"
