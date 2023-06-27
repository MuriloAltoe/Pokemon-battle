from Pokemon import Pokemon
import random

class Batalha:

    def __init__(self):
        self.order = 0
        self.pokemon1 = Pokemon()
        self.pokemon2 = Pokemon()
        pass

    def speedContest(self):
        if self.pokemon1.speed > self.pokemon2.speed:
            self.order = 1
        elif self.pokemon1.speed == self.pokemon2.speed:
            self.order = random.randint(1,3)
        else:
            self.order = 2
        print("poke1: "+ str(self.pokemon1.speed))
        print("poke2: "+ str(self.pokemon2.speed))
        print(self.order)
