from utils.getLink import getJSON
from classe.Type import Type
#
import random

class Pokemon():

    def __init__(self) -> None:
        self.name = ""
        self.type = []
        ...

    def setPokemon(self):
        link = "https://pokeapi.co/api/v2/pokemon/"+str(random.randint(1,151))
        json = getJSON(link)

        self.name = json["name"]

        for i in json["types"]:
            self.type.append(i["type"]["name"])

        ...

    def toString(self):
        print(self.name)




