from utils.getLink import getJSON

class Type():
    def __init__(self) -> None:
        self.name = ""
        self.damageRelations = DamageRelations()
        pass

    def setType(self, id):
        link = "https://pokeapi.co/api/v2/type/"+str(id)
        json = getJSON(link)

        self.name = json["name"]
        self.damageRelations.setDamageRelations(json)

        ...

    def isWeaker(self, otherType): # verificar se o tipo é mais fraco que o parametro
        if otherType in self.damageRelations.halfTo:
            return True
        else:
            return False
        ...

    def isStronger(self, otherType): # verificar se o tipo é mais forte que o parametro
        if otherType in self.damageRelations.doubleTo:
            return True
        else:
            return False
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
        for i in json["damage_relations"]["double_damage_from"]:
            self.doubleFrom.append(i["name"])
            ...
        for i in json["damage_relations"]["double_damage_to"]:
            self.doubleTo.append(i["name"])
            ...
            
        for i in json["damage_relations"]["half_damage_from"]:
            self.halfFrom.append(i["name"]) 
            ...
        for i in json["damage_relations"]["half_damage_to"]:
            self.halfTo.append(i["name"]) 
            ...

        for i in json["damage_relations"]["no_damage_from"]:
            self.noFrom.append(i["name"]) 
            ...
        for i in json["damage_relations"]["no_damage_to"]:
            self.noTo.append(i["name"]) 
            ...