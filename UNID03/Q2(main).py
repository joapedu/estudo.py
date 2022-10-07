## Ultima unidade da disciplina, muitas observações e revisões de arrays
## não lembro a questão!!

import math

n1 = (input())

def n1() -> int:
    return n1

n1: str

lista = []

for _ in range(n1):
    lista.append(int(input()))

for i in lista:
    if i <= n1:
        print("5")
    else:
        print("2")


## Tinha isso aqui no bloco de notas p/ anotações 
nome = str(input())

nomeComEspaco = ""

for i in nome:
  nomeComEspaco += i + " "

nome = nomeComEspaco.strip().split(" ")

for i in range(len(nome)):
  saida = ""
  for j in range(i + 1):
    saida += nome[j]
  print(saida)
