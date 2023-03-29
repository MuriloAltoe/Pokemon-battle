class Pokemon():
    def __init__(self,name,life,atack,defense,spAtack,spDef,speed,type,moves,):
        self.life = life
        self.name = name
        self.atack = atack
        self.defense = defense
        self.spAtack = spAtack
        self.spDef = spDef
        self.speed = speed
        self.type = [type]
        self.moves = [moves]