jour_semaine = int(input("Donnez un jour de la semaine, \n entrez un chiffre, choisir entre 1 à 7:"))
liste_semaine=["k ","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
if jour_semaine==1:
    print(liste_semaine[1])
elif jour_semaine==2:
    print(liste_semaine[2])
elif jour_semaine==3:
    print(liste_semaine[3])
elif jour_semaine==4:
    print(liste_semaine[4])
elif jour_semaine==5:
    print(liste_semaine[5])
elif jour_semaine==6:
    print(liste_semaine[6])
elif jour_semaine==7:
    print(liste_semaine[7])
else :
    print("Veuillez saisir un chiffre entre 1 à 7!!")