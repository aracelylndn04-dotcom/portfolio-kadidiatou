def add_name(names):
    name = input("Entrez un nom à ajouter : ")
    if len(name) != 0:
        names.append(name)
    print("Liste :", names)
    return names

def delete_name(names):
    print("Liste :", names)
    for i in range(len(names)):
        print(str(i) + " - " + names[i])
    num = int(input("Numéro du nom à supprimer : "))
    if num < 0 or num >= len(names):
        print("Numéro invalide")
        return names
    del names[num]
    print("Liste :", names)
    return names
def change_name(names):
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

def view_names(names):
    print("Liste :", names)

def menu():
    names = ["Kadi", "Alissia","Aya","Antoine"]
    choix = ""
    while choix != "0":
        print("1. Pour ajouter des noms dans une liste.\n2. Pour changer des noms dans une liste.\n3. Pour supprimer des noms dans une liste.\n4. Pour afficher la liste.\n0. Pour mettre fin au programme.")
        choix = input("Choix : ")

        if choix == "1":
            names = add_name(names)
        if choix == "3":
            names = delete_name(names)
        if choix == "2":
            names = change_name(names)
        if choix == "4":
            view_names(names)

menu()