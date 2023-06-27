import random
import requests
from Movimento import Movimento

class Pokemon():

    def toString(self,):
        print("Lv" + str(self.level) + " " + str(self.name))
        print("life:" + str(self.life))
        print("Atk:" + str(self.atack))
        print("Def:" + str(self.defense))
        print("Sp. atk:" + str(self.spAtack))
        print("Sp. def:" + str(self.spDef))
        print("Spd:" + str(self.speed))
        print("attacks:\n" + str(self.moves_list[0]) +"\t"+ str(self.moves_list[1]) + "\n" + str(self.moves_list[2]) +"\t"+ str(self.moves_list[3]))

    def __init__(self):
        pokeapi = "https://pokeapi.co/api/v2/pokemon/"+str(random.randint(1,151))
        res = requests.get(pokeapi)
        json = res.json()

        self.level = random.randint(50,76)
        self.name = json["name"]
        self.life = round(json["stats"][0]["base_stat"]*0.03*self.level)
        self.atack = round(json["stats"][1]["base_stat"]*0.03*self.level)
        self.defense = round(json["stats"][2]["base_stat"]*0.03*self.level)
        self.spAtack = round(json["stats"][3]["base_stat"]*0.03*self.level)
        self.spDef = round(json["stats"][4]["base_stat"]*0.03*self.level)
        self.speed = round(json["stats"][5]["base_stat"]*0.03*self.level)
        self.type = []
        self.moves = {}
        self.moves_list = []

        for types in json["types"]:
            self.type.append(types)

        for i in range(4):
            move_ph = json["moves"][random.randint(1,len(json["moves"])-1)]["move"]["url"]
            self.moves[i]= Movimento()
            self.moves[i].leMov(move_ph)

            self.moves_list.append(str(self.moves[i].name))



            
            
            
            
            

        