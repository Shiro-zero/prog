import random
import time

def corps(x):
    if x == 0:
        print(" O")
        print("/|\ ")
        print(" |")
        print("/ \ ")

    if x == 1:
        print(" O")
        print("/|\ ")
        print(" |")
        print("/  ")
    if x == 2:
        print(" O")
        print("/|\ ")
        print(" |")
        print(" ")

    if x == 3:
        print(" O")
        print("/|\ ")
        print(" ")
        print(" ")

    if x == 4:
        print(" O")
        print("/| ")
        print(" ")
        print(" ")

    if x == 5:
        print(" O")
        print(" | ")
        print(" ")
        print(" ")

    if x == 6:
        print(" O")
        print(" ")
        print(" ")
        print(" ")

    if x == 7:
        print("perdu le mot etait", mot)
        exit()


mot = ""
alphabet = ["m", "a", "t", "e", "o", "d", "l", "c", "n", "k", "u", "b", "s", "h", "i", "x", "y", "z", "q", "j", "r", "v", "w", "f", "g", "p"]
liste_mot = open("assets/liste_francais.txt")
for i in range(random.randint(0, 22740)):
    mot = liste_mot.readline()
lmot = len(mot)

a = []
w = 0
hp = 0
x = 0

for i in range(lmot-1):
    a += "_"

while a != mot:
    lettre = str(input("une lettre:"))
    for m in range(lmot):
        if lettre == mot[m]:
             a[m] = lettre
        else:
            x += 1
    if x == lmot:
        hp += 1
    x = 0
    print(a)
    corps(hp)
