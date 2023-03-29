import random
import requests
import Pokemon

def escolheMovimentos(moveList, moveSet):
    for i in range(4):
        moveSet[i] = moveList[random.randint(1,len(moveList))]

def criaPokemon(pokebola):
    pokeapi = "https://pokeapi.co/api/v2/pokemon/"+str(random.randint(1,151))
    res = requests.get(pokeapi)
    json = res.json()

    pName = json["name"]

    pType = []
    for types in json["types"]:
        pType.append(types)

    pMoves = {}
    type(pMoves)
    escolheMovimentos(json["moves"], pMoves)

#   pokebola = Pokemon(pName,pLife,pAtk,pDefense,sSpAtk,SpDef,pSpeed,pType,pMoves)
    print(pName)
    print(pType)
    print(pMoves)


pokemon1 = ''

criaPokemon(pokemon1)
