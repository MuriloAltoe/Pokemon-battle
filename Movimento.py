import requests

class Movimento():

    def __init__(self):
        self.name = ''
        self.acc = ''
        self.dmg = ''
        self.type = {}

    def leMov(self, moveLinkApi):
        pokeapi = moveLinkApi
        res = requests.get(pokeapi)
        json = res.json()
        self.name = json["name"]
        self.acc = json["accuracy"]
        self.dmg = json["power"]
        self.type = json["type"]

    def toString(self,):
        print(self.name)
        print(self.acc)
        print(self.dmg)
        print(self.type)
