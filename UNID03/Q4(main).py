#Ultima unidade da disciplina, muitas observações e revisões de arrays
#Parece incompleta e dividida em duas partes
#Confuso, não lembro a questão
#Colocar issue pra investigar, terminar e juntar as partes

#primeira parte
import math

valor = int(input())

produto = []

produto.append(input())

for i in produto:
  if sum(produto) / valor % 0:
    print("OK")
  else:
    print("OVERFLOW")

#segunda parte

N = int(input())

lista = []

for i in range(N):
  leitura = input()
  if not(leitura in lista):
    lista.append(leitura)

print(" ".join(lista))
