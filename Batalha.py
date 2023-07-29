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

        # print("poke1: "+ str(self.pokemon1.speed))
        # print("poke2: "+ str(self.pokemon2.speed))
        # print(self.order)

    def showBattle(self):
        line1 = "Lv " + str(self.pokemon1.level) + " " + str(self.pokemon1.name)
        line2 = "Life: " + str(self.pokemon1.actualLife) + "/" + str(self.pokemon1.life)
        line3 = (
            str(self.pokemon1.moves[0].actualPp) + "/" + str(self.pokemon1.moves[0].pp) + " - " + str(self.pokemon1.moves[0].name) + " | " + 
            str(self.pokemon1.moves[1].actualPp) + "/" + str(self.pokemon1.moves[1].pp) + " - " + str(self.pokemon1.moves[1].name) + " | " +
            str(self.pokemon1.moves[2].actualPp) + "/" + str(self.pokemon1.moves[2].pp) + " - " + str(self.pokemon1.moves[2].name) + " | " +
            str(self.pokemon1.moves[3].actualPp) + "/" + str(self.pokemon1.moves[3].pp) + " - " + str(self.pokemon1.moves[3].name)
        )

        print(line1+"\n"+line2+"\n"+line3)

        line1 = "Lv " + str(self.pokemon2.level) + " " + str(self.pokemon2.name)
        line2 = "Life: " + str(self.pokemon2.actualLife) + "/" + str(self.pokemon2.life)

        print(line1+"\n"+line2)
        

