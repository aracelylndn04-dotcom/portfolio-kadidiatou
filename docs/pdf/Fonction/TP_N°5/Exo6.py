
def add_name(liste_name):
    name=input("Entrez un nom :")
    if len(name) !=0:
        liste_name.append(name)
        print(liste_name)

liste_name=[]        
add_name(liste_name)
