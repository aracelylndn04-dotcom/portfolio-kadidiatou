def delete_name():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    print("Liste des noms :",names)
    for i in range(len(names)):
        print(str(i) + " - " + names[i])
    num = int(input("Entrez le numéro du nom à supprimer : "))
    if num < 0 or num >= len(names):
        print("Numéro invalide !")
        return names
    else:
        del names[num]
    print("Liste modifiée :",names)
    return names
names = delete_name()
