from math import *
from random import *
#import math 

print("Puu läbimõõdu arvutamine")
#1Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.

C=float(input("Anna ümbermõõt: "))
d=round(C/pi,2)
print(f"Puu läbimõõt = {d}")

#2Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.

print("Ristküliku omadused")
M=float(input("Ristküliku esimene külg ->"))
N=float(input("Ristküliku teine külg ->"))
c=sqrt(N**2+M**2)
print("Ristiküliku pikkus on", round(c,2))
print()

#3Leidke järgnevast näiteprogrammist semantiline viga

aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus
print("Sinu kiirus oli" + str(kiirus) + "km/h")
print()

#4Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.

print("määrage viis täisarvus")
a=int(input("Sisestage esimene täisarv -> "))
b=int(input("Sisestage teine täisarv -> "))
c=int(input("Sisestage kolmas täisarv -> "))
d=int(input("Sisestage neljas täisarv -> "))
e=int(input("Sisestage viias täisarv -> "))
h=(a+b+c+d+e)/5
print("Aritmeetilise keskmise", h)

#5Joonista samasugune konn

print("@..@")
print("(----)")
print("( \__/ )")
print("^^ "" ^^")

#6Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)

a=randint(0,100)
b=randint(0,100)
c=randint(0,100)
print(f"a={a}\n,b={b}\n,c={c}")
P=a+b+c 
print(f"ümbermõõt on {P}")

#7Pitsa

P=randint(1,6)
summa=(12.9*1.1)/P
print(f"{P}-st, Igaüks maksab {summa}")

#8Kütusekulu arvutamine

print("Kütusekulu arvutamine")
l=float(input("Kütuse liitride kogus: "))
km=float(input("Läbitud kilomeetrid: "))
kulu=(l/km)*100
print(f"Kütusekulu arvutamine 100 km kohta on võrdne: {kulu}")

#9Rulluisutajad

print("Rulluisutajad")
M=int(input("Minutid:"))
M=M/60
tee=M*29.9
print(f"Jõuab {tee} km")

#10Ajateisendus

print("Ajateisendus")
M=int(input("Sisesta aja minutites")) #h=60 min
H=M//60 #h
M=M%60 #min
