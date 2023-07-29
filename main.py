from Pokemon import Pokemon
from Batalha import Batalha

print("Oque quer fazer? \n 1- Gerar um pokemon aleatório \n 2- Batalhar")
escolha = int(input())

if escolha == 1:
    pokemon1 = Pokemon()
    pokemon1.toString()
elif escolha == 2:
    batalha = Batalha()
    batalha.speedContest()

    batalha.showBattle()
    pass
