from utils.getLink import getJSON

class Type():
    def __init__(self) -> None:
        self.name = ""
        self.damageRelations = DamageRelations()
        pass

    def setType(self, id):
        link = "https://pokeapi.co/api/v2/type/"+id
        json = getJSON(link)

        self.name = json["name"]
        self.damageRelations.setDamageRelations(json)

        ...

    def checkType(self, otherType): #TODO: verificar se o tipo é mais forte que o parametro
        ...


class DamageRelations():
    def __init__(self) -> None:
        self.doubleTo = []
        self.doubleFrom = []
        self.halfTo = []
        self.halfFrom = []
        self.noTo = []
        self.noFrom = []

        ...

    def setDamageRelations(self, json):
#
        for i in json["damage_relations"]["double_damage_from"]:
            self.doubleFrom.insert(i["name"])
            ...
        for i in json["damage_relations"]["double_damage_to"]:
            self.doubleTo.insert(i["name"])
            ...
#
        for i in json["damage_relations"]["half_damage_from"]:
            self.halfFrom.insert(i["name"]) 
            ...
        for i in json["damage_relations"]["half_damage_to"]:
            self.halfTo.insert(i["name"]) 
            ...
#
        for i in json["damage_relations"]["no_damage_from"]:
            self.noFrom.insert(i["name"]) 
            ...
        for i in json["damage_relations"]["no_damage_to"]:
            self.noTo.insert(i["name"]) 
            ...