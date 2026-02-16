Heure_travail=int(input("Entrez l'heure de travail que vous avez effectuer:"))
prix_par_heure=int(input("Entrez le prix unitaire par heure de travail:"))
montant=Heure_travail*prix_par_heure
if Heure_travail>=40 and Heure_travail<=44:
    montant=(Heure_travail-39)*(prix_par_heure*1.5)
    print("Vous avez",montant,"euros obetenu par H avec 4h de travail supplémentaire.")
elif Heure_travail>=45 and Heure_travail<=49:
    montant=(5*prix_par_heure*1.5)+(Heure_travail-44)*(prix_par_heure*1.75)
    print("Vous avez",montant,"euros obetenu par H avec 9h de travail supplémentaire.")
elif Heure_travail>=50:
    montant=(5*prix_par_heure*1.5)+(Heure_travail-44)+(prix_par_heure*1.75)*(Heure_travail-49)*(prix_par_heure*2)
    print("Vous avez",montant,"euros obetenu par H avec 10h de travail supplémentaire.")
else:
    print("Vous avez",montant,"euros obtenu par H de travil")

