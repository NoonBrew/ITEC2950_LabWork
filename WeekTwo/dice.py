import random

class Dice:
    # Default values handy for when an object has a common value
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

dice = Dice(6)

print(dice.roll())