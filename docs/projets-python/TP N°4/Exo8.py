date_valide = False
print("CONDITIONS :\nTous les saisit sont faits avec des chriffres.")
while date_valide == False:

    jour = int(input("Entrez le jour : "))
    mois = int(input("Entrez le mois : "))
    annee = int(input("Entrez l'année : "))
    jours_max = 0
    if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12 and annee<=2025:
        jours_max = 31
    elif mois == 4 or mois == 6 or mois == 9 or mois == 11:
        jours_max = 30
    elif mois == 2:
        if (annee % 4 == 0 and annee % 100!=0) or annee %400==0:
            jours_max = 29
        else:
            jours_max = 28
    else:
        print("Mois invalide.")
    if jour >= 1 and jour <= jours_max and annee<=2025 and mois>=1 and mois <=12:
        print("La date est correcte :",jour,"/",mois,"/",annee)
        date_valide = True
    else:
        print("Jour invalide pour ce mois, recommencez.")

