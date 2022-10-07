# questão 2 lista de exercícios facul

import math

base = float(input())

provas = 0
quantidade = 0
n = 0

while(True):
  t = float(input())
  if t == -1.0:
    break
  if base > t:
    quantidade = quantidade + 1

print(quantidade)

print(math.ceil(quantidade/8))
