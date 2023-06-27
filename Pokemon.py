import random
import requests
from Movimento import Movimento

class Pokemon():
    def __init__(self):
        pokeapi = "https://pokeapi.co/api/v2/pokemon/"+str(random.randint(1,151))
        print(pokeapi)
        res = requests.get(pokeapi)
        json = res.json()

        self.level = random.randint(50,76)
        print(self.level)
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

            # self.moves[i].toString()

    def toString(self,):
        print("nome:" + str(self.name))
        print("life:" + str(self.life))
        print("atack:" + str(self.atack))
        print("defesa:" + str(self.defense))
        print("spatk:" + str(self.spAtack))
        print("spdef:" + str(self.spDef))
        print("speed:" + str(self.speed))
        print("attacks:" + str(self.moves_list))



            
            
            
            
            

        