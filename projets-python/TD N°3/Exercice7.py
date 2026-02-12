import random


liste=["Vert","Jaune","Blanc","Rouge","Bleu"]
extraterreste_immobilise=random.choice(liste)
print(extraterreste_immobilise)
if extraterreste_immobilise==liste[0]:
    print("Vous venez de gagné 5 points.")
else :
    print("Vous venez de gagner 10 points.")
