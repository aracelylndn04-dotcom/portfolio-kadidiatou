voyelle = ["i","u","o","a","e","é","è","ê","y"]
print("Les conditions de validités de mot de passe:\n1)Votre mot de passe doit contenir entre 6 à 10 chriffres.")
print("2)Il doit contenir des chriffres (entre 1 à 20) et lettres.\n3)Le premier caractère doit être une voyelle.")
mot_de_passe = input("Entrez un mot de passe:")
premier=mot_de_passe[0]
correct=False
while correct==False:
    if premier in voyelle and len(mot_de_passe)>=6 and len(mot_de_passe)<=10:
            correct=True
            print("Votre mot de passe est correct\nVoici votre nouveau mot de passe:",mot_de_passe)
    else:
        correct=False
        print("Veuillez svp entrer un mot de passe en respectant les conditions!!")
        mot_de_passe = input("Entrez un mot de passe:")
        premier=mot_de_passe[0]