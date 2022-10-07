# prova fisica questão 6 facul

import math

votos = []

for _ in range(1000):
  leitura = int(input())
  if leitura == 0:
    break
  else:
    votos.append(leitura)

w = (votos.count(1))
w = (100*w)/len(votos)

u = (votos.count(2))
u = (100*u)/len(votos)

l = (votos.count(3))
l = (100*l)/len(votos)

m = (votos.count(5))
m = (100*m)/len(votos)

n = (votos.count(4))
n = (100*n)/len(votos)

o = (votos.count(6))
o = (100*o)/len(votos)

if 1 in votos:
  if(votos.count(1) > 1):
    print("Windows,",(votos.count(1)),"votos,", str(int(w))+"%")
  else:
    print("Windows,",(votos.count(1)),"voto,", str(int(w))+"%")

if 2 in votos:
  if (votos.count(2) > 1):
    print("Unix,",(votos.count(2)),"votos,", str(int(u))+"%")
  else:
    print("Unix,",(votos.count(2)),"voto,", str(int(u))+"%")

if 3 in votos:
  if (votos.count(3) > 1):
    print("Linux,",(votos.count(3)),"votos,", str(int(l))+"%")
  else:
    print("Linux,",(votos.count(3)),"voto,", str(int(l))+"%")

if 4 in votos:
  if (votos.count(4) > 1):
    print("Netware,",(votos.count(4)),"votos,", str(int(n))+"%")
  else:
    print("Netware,",(votos.count(4)),"voto,", str(int(n))+"%")

if 5 in votos:
  if (votos.count(5) > 1):
    print("MacOS,",(votos.count(5)),"votos,", str(int(m))+"%")
  else:
    print("MacOS,",(votos.count(5)),"voto,", str(int(m))+"%")

if 6 in votos:
  if (votos.count(6) > 1):
    print("Outro,",(votos.count(6)),"votos,", str(int(o))+"%")
  else:
    print("Outro,",(votos.count(6)),"voto,", str(int(o))+"%")

print("Total:", len(votos), "votos")

##para o vencedor
quantVotos = [votos.count(1), votos.count(2), votos.count(3), votos.count(4), votos.count(5), votos.count(6)]

sistemas = ["Windows", "Unix", "Linux", "Netware", "MacOS", "Outro"]

maior = 0

for i in quantVotos:
    if(maior < i):
        maior = i

for i in range(len(sistemas)):
    if(quantVotos[i] == maior):
        if(i == len(sistemas)):
            print("Vencedor:", sistemas[i], "com", str(int((100*maior)/len(votos))) + "%", "dos votos")
        else:
            print("Vencedor:", sistemas[i], "com", str(int((100 * maior) / len(votos))) + "%", "dos votos ")
