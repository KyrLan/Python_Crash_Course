from random import randint
class Die():
    def __init__(self, sides):
        self.sides = sides
    def roll_die(self, rolling):
        self.rolling = rolling
        roll_value = []
        for i in range (0, self.rolling):
            x = randint(1, self.sides)
            roll_value.append(x)
        print (roll_value)

six_edge = Die(6)
six_edge.roll_die(10)

ten_edge = Die(10)
ten_edge.roll_die(10)

twenty_edge = Die(20)
twenty_edge.roll_die(10)