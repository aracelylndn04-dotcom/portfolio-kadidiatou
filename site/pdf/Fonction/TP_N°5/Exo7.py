def change_name():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    print("Liste des noms :",names)
    for i in range(len(names)):
        print(str(i) + " - " + names[i])
    num = int(input("Entrez le numéro du nom à modifier : "))

    if num < 0 or num >= len(names):
        print("Numéro invalide !")
        return names


    new_name = input("Entrez le nouveau nom : ")
    names[num] = new_name

    print("Liste modifiée :",names)
    return names
names = change_name()