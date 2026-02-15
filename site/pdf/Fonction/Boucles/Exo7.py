
continuer = False
while continuer == False:
    name = input("Saississez le nom de la personne que vous voulez inviter :")
    print(name,"a maintenant été invité!")
    invitation = input("Souhaitez vous inviter d'autres personnes?\nRépondez oui ou non.")
    if invitation == "non":
        continuer= True
        