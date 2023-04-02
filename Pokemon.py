import random
import requests
from Movimento import Movimento

class Pokemon():
    def __init__(self):
        pokeapi = "https://pokeapi.co/api/v2/pokemon/"+str(random.randint(1,151))
        res = requests.get(pokeapi)
        json = res.json()

        self.level = random.randint(50,76)
        self.name = json["name"]
        self.life = json["stats"][0]["base_stat"]
        self.atack = json["stats"][1]["base_stat"]
        self.defense = json["stats"][2]["base_stat"]
        self.spAtack = json["stats"][3]["base_stat"]
        self.spDef = json["stats"][4]["base_stat"]
        self.speed = json["stats"][5]["base_stat"]
        self.type = []
        self.moves = {}

        for types in json["types"]:
            self.type.append(types)

        for i in range(4):
            move_ph = json["moves"][random.randint(1,len(json["moves"])-1)]["move"]["url"]
            self.moves[i]= Movimento()
            self.moves[i].leMov(move_ph)
            self.moves[i].toString()

    # def toString(self,):
    #     print("nome:" + str(self.name))
    #     print("life:" + str(self.life))
    #     print("atack:" + str(self.atack))
    #     print("defesa:" + str(self.defense))
    #     print("spatk:" + str(self.spAtack))
    #     print("spdef:" + str(self.spDef))
    #     print("speed:" + str(self.speed))


            
            
            
            
            

        