# prova fisica questão 8 facul

import math

N = int(input())

list = []

for i in range(N):
  leitura = int(input())
  list.append(leitura)

P = int(input())

indexMenor = P

menorCusto = 0

for i in range(N):
  if(i == P): continue
  custo = 10 * (P - i if P > i else i - P) + 10 * list[i]
  if menorCusto == 0 or menorCusto > custo:
    menorCusto = custo
    indexMenor = i

print(indexMenor)
