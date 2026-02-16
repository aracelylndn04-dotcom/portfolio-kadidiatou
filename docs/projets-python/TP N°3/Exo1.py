print("Choisissez une option :")
print("1 pour la muslitiplacation")
print("2 pour l'addition")
print("Et 3 pour la soustraction")
choix = input("Entrez 1, 2 ou 3 : ")

if choix =="1":
    multiplacation1 =int(input("Entrez un 1er chiffre: "))
    multiplacation2 = int(input("Entrez un 2ème chiffre: "))
    multiplacation = multiplacation1 * multiplacation2
    print("La multiplication de ces deux chiffres est :", multiplacation)
elif choix =="2":
    l_addition1 = int(input("Entrez un 1er chriffre: "))
    l_addition2 = int(input("Entrez un 2ème chriffre: "))
    l_addition = l_addition1 + l_addition2
    print("L'addition de ces 2 chiffres est :",l_addition)
elif choix == "3":
    La_soustraction1= int(input("Entrez un 1er chiffre: "))
    La_soustraction2 =  int(input("Entrez un 2ème chriffre: "))
    La_soustraction = La_soustraction1 - La_soustraction2
    print("La soustraction de ces 2 chiffres est :",La_soustraction)

else:
    print("Option invalide. Veuillez entrer 1,2 ou 3")
