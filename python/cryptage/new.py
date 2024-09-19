import random
import time
#action = int(input("coder = 0 décoder = 1\n"))

def crypt(mot=input("ce que tu veux coder\n")):
    deplacement = -1
    mot_ord =[]
    mot_crypte = ""
    decalage = random.randint(-126,126)
    if decalage<0:# si décalage est négatif on atribue 1 pour pouvoir décrypter le négatif puis on ajute le décalage en positife 
        mot_ord.append(1)
        mot_ord.append(-decalage)# si c'est trop petit ou trop grand on renvoix de l'autre coté 
    if decalage >= 0:
        mot_ord.append(decalage)
    for i in range(len(mot)):
        if 16<ord(mot[i])+decalage:
            deplacement=ord(mot[i])+decalage + 16 +126
        
        if 126<ord(mot[i])+decalage:
            deplacement=ord(mot[i])+decalage - 126 + 16
            
        if 16<ord(mot[i])+decalage<126 or decalage == -1:
            deplacement = decalage
            
        if 27 == ord(mot[i])+decalage:
            deplacement = 2
            
        if random.randint(1,20) == 20:
            mot_ord.append(chr(random.randint(3,6))) 
            
        mot_ord.append(deplacement)
    for x in range(len(mot_ord)):# on trensforme en char
        mot_crypte += chr(mot_ord[x])
    print (decalage)
    print(mot_crypte)
        
if False:
    mot=input("ce que tu veux décoder\n")
    mot_decrypte = []
    if chr(mot[0]) == 1: #si c'est négatif on met en négatif
         decalage = -chr(mot(1))
         mot = mot.lstrip(mot[0])
         mot = mot.lstrip(mot[0])
    if chr(mot[0]) != 1:
         decalage = chr(mot(0))
         mot = mot.lstrip(mot[0])
    for i in range(len(mot)):
        mot_ord = chr(ord(mot[i])+decalage)
        mot_decrypte += mot_ord
    print(mot_decypte)
         
    


if False:
    for i in range(-127,127):
        for j in range (16):
            print(j+i+ 16 +126)
            time.sleep(.1)
        #print(i,"=", chr(i))


crypt()