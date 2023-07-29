import requests

class Movimento():
    
    def leMov(self, moveLinkApi):
        pokeapi = moveLinkApi
        res = requests.get(pokeapi)
        json = res.json()
        self.name = json["name"]
        self.acc = json["accuracy"]
        self.dmg = json["power"]
        self.type = json["type"]
        self.pp = json["pp"]
        self.actualPp = self.pp

    def toString(self,):
        print(self.name)
        print(self.acc)
        print(self.dmg)
        print(self.type['name'])

    def __init__(self):
        self.name = ''
        self.acc = ''
        self.dmg = ''
        self.type = {}

    