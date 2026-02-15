nom_prenom= input("Entrez vos noms et prenom séparés par un espace : ")
nom = nom_prenom.split(" ")[0]
a = nom[0].upper()
prenom = nom_prenom.split(" ")[1]
b = prenom[0].upper()
print(a,b)