from utils.getLink import getJSON
from classe.Type import Type
from classe.Move import Move
#
import random

class Pokemon():

    def __init__(self) -> None:
        self.name = ""
        self.type = []
        self.moves = {}
        self.stats = {}
        ...

    def setPokemon(self):
        link = "https://pokeapi.co/api/v2/pokemon/"+str(random.randint(1,151))
        json = getJSON(link)

        self.name = json["name"]

        for i in json["types"]:
            self.type.append(i["type"]["name"])
        ...

        for i in range(0,4):
            rand = random.randint(1, len(json["moves"]))
            move = Move()
            move.setMove(rand)
            self.moves[move.name] = { "pp": move.pp, "damage_class": move.damageClass, "priority": move.priority }
        ...

        for i in json["stats"]:
            self.stats = {i["stat"]["name"]: i["base_stat"]}            
        ...

    # def atack(self, move, target:list):
        





