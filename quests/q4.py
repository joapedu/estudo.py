# questão 4 lista de exercícios facul

import math

n = int(input())

soma = 0

for i in range(1, int(n/2) + 1):
  if n % i == 0: 
    soma = soma + i

if(soma == n):
  print("número perfeito")

else:
  print("número não é perfeito")
