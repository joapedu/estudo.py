## Ultima unidade da disciplina, muitas observações e revisões de arrays

import math

lista = []
for _ in range(5):
  lista.append(int(input()))
lista.remove(max(lista))
lista.remove(min(lista))
print(sum(lista))
lista1 = []
lista2 = []

##     !! [OBS FUNÇÕES]  !!
def say_hi(name, age):
  print("Hello " + name + ", you are " + age)

say_hi("Mike", "35")
say_hi("Steve", "70")

## definição básica da função por meio do print (aplicado a duas funções[name][age])

def cube(num):
  return num*num*num

resultado = cube(3)
print(resultado)
## return tem função de parar o código, além de defini-lo como um todo



##     !! [OBS Lista]  !! 
lista1.extend(lista2)
## adciona uma lista a outra

lista.insert(1, "arroz")
## adciona um elemento no lugar a sua escolha(lista começa em 0)

lista.remove("arroz")
## remove um elemento da lista

lista.clear()
## limpa a lista - deixa em branco

lista.index("arroz")
## fala a posição do elemento "arroz" dentro da lista.

lista.count("arroz")
## conta quantas vezes aparece o elemento arroz dentro da lista

lista.sort()
## coloca a lista:
#           em ordem alfabética(LETRAS)         #
#           em ordem crescente(NÚMEROS)         #

lista.reverse
## reverte a ordem da lista


# EXEMPLOS -> (QUANTOS LIDOS)
n = int(input())

media = 0

lista = []

for _ in range(n):
  lista.append(float(input()))

print("Foram lidos " + str(n) + " valores")

print(lista)
lista.reverse()

print("Lista reversa: ", lista)

media = sum(lista) / len(lista)

print("Média dos valores: ", round(media, 2))

for i in lista:
  if i >= media:
    contador =+ 1

print(contador , "valores acima da média", round(media, 2))
