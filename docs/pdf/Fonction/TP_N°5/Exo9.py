names=["Alice", "Bob", "Charlie", "Diana"]
def add_name(liste_name):
    name=input("Entrez un nom :")
    if len(name) !=0:
        liste_name.append(name)
        print(liste_name)
liste_name=[]        
add_name(liste_name)


def change_name():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    print("Liste des noms :",names)
    for i in range(len(names)):
        print(str(i) + " - " + names[i])
    num = int(input("Entrez le numéro du nom à modifier : "))
    if num < 0 or num >= len(names):
        print("Numéro invalide !")
        return names
    names = change_name()
    new_name = input("Entrez le nouveau nom : ")
    names[num] = new_name
    print("Liste modifiée :",names)
    return names


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

def view_names ():
    print("La liste des noms :",names)