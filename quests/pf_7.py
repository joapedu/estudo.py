# prova fisica questão 7 facul

import math

nomes = []

nota = []

acima = []

for i in range(5):
  nomes.append(input())
  nota.append(int(input()))

media = sum(nota)/5

print(f"Média: {media:.1f}")

for i in range(len(nota)):
  if nota[i] > media:
    acima.append(nomes[i])

print("Acima da média:", ",".join(acima))

print("Maior nota:", nomes[nota.index(max(nota))])
