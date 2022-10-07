# prova fisica questão 5 facul

import math

lista = []

for i in range(10):
  lista.append(int(input()))

lista.sort()

t = ""

for i in lista:
  t = (t + (" ") + str(i))

print(t.strip())
