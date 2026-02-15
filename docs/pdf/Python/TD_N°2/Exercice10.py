semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
print("Liste des jours :", semaine)
print("Jour à l'indice 4 est :", semaine[4])
premier = semaine[0]
dernier = semaine[-1]
semaine.remove(premier)
semaine.remove(dernier)
semaine.insert(0, dernier)
semaine.insert(len(semaine), premier)
print("Liste après échange :", semaine)