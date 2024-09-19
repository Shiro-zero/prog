#Code Bastien Dauger, Victor Schalke, Maximilian Lopez

import random

caractere = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
dicocaractere = {" ":0,"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,"0":27,"1":28,"2":29,"3":30,"4":31,"5":32,"6":33,"7":34,"8":35,"9":36,"A":37,"B":38,"C":39,"D":40,"E":41,"F":42,"G":43,"H":44,"I":45,"J":46,"K":47,"L":48,"M":49,"N":50,"O":51,"P":52,"Q":53,"R":54,"S":55,"T":56,"U":57,"V":58,"W":59,"X":60,"Y":61,"Z":62}

def vigenere(phrase, cle): #code vigenère
    phraselist = []
    N = 0
    for loop in phrase:  #on calcule les caractere valide
        for loop2 in dicocaractere.keys():
            if loop == loop2:
                N += 1
        phraselist.append(loop)
    if not N == len(phrase): #on les compare avec la longueur de la list
        print("probleme")
        exit()
    boucle = 0
    fin = []
    nbcle = 0
    while boucle < len(phraselist):  #Convertie la phrase en nombre
        lettre = (dicocaractere.get(cle[nbcle]) + dicocaractere.get(phraselist[boucle])) #additionne la lettre avec la clé
        if lettre > 62: #test si l'addition ne sort pas du cadre et remet dans un format valide
            lettre -= 63
        boucle += 1
        nbcle = boucle
        nbcle = nbcle%len(cle) #quand la clé vient de se finir, elle revient à 0
        fin.append(str(lettre)) #Ajoute à une list les lettre cryptée mais en nombre
    result = ""
    newcle = ''
    for loop in fin: #Convertie en lettre
        result += caractere[int(loop)]
    for loop in cle: #donne une forme lisible de la clé
        newcle = newcle + str(loop)
    print("La clé est "+newcle+" et donne comme phrase cryptée:"+result)

def decodagevige(phrase, cle): #Décrypte le code vigenere
    phraselist = []
    N = 0
    for loop in phrase: #on calcule les caractere valide
        for loop2 in dicocaractere.keys():
            if loop == loop2:
                N += 1
        phraselist.append(loop)
    if not N == len(phrase):  #on les compare avec la longueur de la list
        print("probleme")
        exit()
    boucle = 0
    fin = []
    nbcle = 0
    while boucle < len(phraselist):   #Convertie la phrase en nombre
        lettre = (dicocaractere.get(phraselist[boucle]) - dicocaractere.get(cle[nbcle])) #soustrait la lettre cryptée avec la clé
        if lettre < 0:  #test si la soustraction ne sort pas du cadre et remet dans un format valide
            lettre += 63
        boucle += 1
        nbcle = boucle
        nbcle = nbcle % len(cle) #quand la clé vient de se finir, elle revient à 0
        fin.append(str(lettre)) #Ajoute à une list les lettre décryptée mais en nombre
    result = ""
    for loop in fin:  #Convertie en lettre
        result += caractere[int(loop)]
    print("La phrase décryptée donne:", result)

def decalage(mdp, decalage1):
    if decalage1>=64:
        return('Decalage trop grand')
    mdp1=[]
    for i in mdp:
        e=0
        for j in caractere:
            if j==i:
                f=e+decalage1
                mdp1.append(caractere[f])
            else:
                e=e+1
                if e>62-decalage1:
                    e=e-63
    result = ""
    t=0
    for loop in mdp1:
        result += mdp1[t]
        t=t+1
    print("La phrase cryptée donne:", result)

def decalagedecodage(mdp, decalage):
    if decalage>=64:
        return('Decalage trop grand')
    mdp1=[]
    for i in mdp:
        e=0
        for j in caractere:
            if j==i:
                f=e-decalage
                mdp1.append(caractere[f])
            else:
                e=e+1
                if e>62-decalage:
                    e=e-63
    result = ""
    t=0
    for loop in mdp1:
        result += mdp1[t]
        t=t+1
    print("La phrase décryptée donne:", result)


print("Vous avez le choix entre 4 posibilités: ")
print("1-Chiffrer une suite de caractere avec le codage vigenere avancé")
print("2-Déchiffrez une suite de caractere chiffrez avec le code vigenere avancé(la clé est requise)")
print("3-Chiffrer une suite de caractere avec le codage caesar ")
print("4-Déchiffrez une suite de caractere avec le codage caesar (Décalage requis)")
choix = int(input("Que choisisez-vous: "))

if choix == 1:
    phrase = str(input("Quelle phrase voudriez-vous chiffrez ? (espaces, minuscules, majuscules et chiffres seulement) "))
    cle = str(input("Introduisez une clé : (rien mettre pour en généré une aléatoirement) "))
    if cle == "": #crée une clé aléatoire
        cle = []
        for loop in range(20):
            cle += caractere[random.randint(0, 62)]
    else: #converti la clé en list
        a = cle
        cle = []
        for loop in a:
            cle.append(loop)
    vigenere(phrase, cle)

if choix == 2:
    phrase = str(input("Quelle phrase voudriez-vous déchiffrez (espaces, minuscules, majuscules et chiffres seulement): "))
    cle = str(input("Introduisez votre clé de déchiffrage: "))
    decodagevige(phrase, cle)

if choix == 3:
    mdp = str(input("Quelle phrase voudriez-vous déchiffrez (espaces, minuscules, majuscules et chiffres seulement): "))
    decalage2 = int(input("Introduisez votre décalage: "))
    decalage(mdp , decalage2)

if choix == 4:
    phrase = str(input("Quelle phrase voudriez-vous déchiffrez (espaces, minuscules, majuscules et chiffres seulement): "))
    decalage = int(input("Introduisez votre décalage: "))
    decalagedecodage(phrase, decalage)