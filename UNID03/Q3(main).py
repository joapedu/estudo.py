#Ultima unidade da disciplina, muitas observações e revisões de arrays
#Parece incompleta e dividida em duas partes
#Confuso, não lembro a questão
#Colocar issue pra investigar, terminar e juntar as partes

#primeira parte
import math

lista = []
n = int(input())
for i in range(n):
  lista.append(input)
j = n / 2
print(j)


#segunda parte
numero = int(input())

def calcular(nota):
  numeroLocal = numero
  if(numero // nota != 0):
    quantNota = 0
    while True:
      if(numeroLocal // nota != 0):
        numeroLocal = numeroLocal - nota
        quantNota += 1
      else:
        break
    print(quantNota, "de", nota)
    return numeroLocal
  else:
    print(0, "de", nota)
    return numeroLocal

numero = calcular(100)
numero = calcular(50)
numero = calcular(20)
numero = calcular(10)
numero = calcular(5)
numero = calcular(2)
numero = calcular(1)
