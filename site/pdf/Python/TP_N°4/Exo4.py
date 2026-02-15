import random
print("Les règles du jeu :\n")
print("Si le nombre tiré est pair vous gagnez 1 euros, \nou si le nombre tiré se termine par 7 vous gagnez 10 euros \ndans les cas contraire vous perdez 3 euros.")
compteur = 0
choix="oui"
while choix == "oui":
    a = random.randint(1,100)
    print(a)
    if a%2==0:
        compteur = compteur+1
        print("Vous avez gagnez",compteur,"euros.")
        
    elif str(a)[-1]=="7":
        compteur = compteur + 10
        print("Vous avez gagnez",compteur,"euros")
        
    else:
        compteur = compteur - 3
        print("Vous avez perdu",compteur,"euros.")
    print("Voulez vous continuer?")
    choix=input("Choissisez oui ou non!").lower()
print("Fin du jeu")        