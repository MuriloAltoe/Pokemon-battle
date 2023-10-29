from classe.Pokemon import Pokemon

class Battle():

    def __init__(self) -> None:
        self.atacker = ""
        self.target = ""
    ...

    def atack(self, atacker:Pokemon, target:Pokemon):
        self.atacker = atacker
        self.target = target



