from utils.getLink import getJSON

class Move():
    def __init__(self) -> None:
        self.name = ""
        self.damageClass = ""
        self.priority = 0
        self.type = ""
        self.power = 0
        self.pp = 0
        pass

    def setMove(self, id):
        link = "https://pokeapi.co/api/v2/move/"+str(id)
        json = getJSON(link)

        self.pp = json["pp"]
        self.name = json["name"]
        self.damageClass = json["damage_class"]["name"]
        self.priority = json["priority"]
        self.type = json["type"]["name"]

        ...
