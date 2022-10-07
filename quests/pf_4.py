# prova fisica questão 4 facul

import math

M = int(input())
D = int(input())

divisiveis = []

a = 0
b = 1

while len(divisiveis) < M:
  S = a + b
  if S % D == 0:
    divisiveis.append(S)
  a = b
  b = S

for i in divisiveis:
  print (i)
