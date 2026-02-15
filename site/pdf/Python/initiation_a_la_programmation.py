conditions = True
while conditions == True:
    print("Bienvenue au distributeur automatique de boissons.")
    print("Pour commander un café, tapez le chiffre 1. Le café coûte 2 euro.")
    print("Pour commander un thé, tapez le chiffre 2. Le thé coûte 1.5 euros.")
    print("Pour commander un jus d'orange, tapez le chiffre 3. Le jus d'orange coûte 2.5 euros.")
    choix = input("Tapez ici votre choix : ")
    boisson=""
    prix_cafe = 2
    prix_the = 1.5
    prix_jus = 2.5
    if choix == "1":
        prix = prix_cafe
        boisson = "café"
    elif choix == "2":
        prix = prix_the
        boisson = "thé"
    elif choix == "3":
        prix = prix_jus
        boisson = "jus d'orange"
    else:
        print("Vous avez fait un choix qui n'existe pas dans le menu.")

    print("Vous avez choisi :", boisson, ". Le prix est de", prix, "euros.")
    argent = float(input("Tapez le montant d'argent que vous mettez dans la machine : "))
    if argent >= prix:
        rendu = argent - prix
        print("Votre boisson est servie :", boisson)
        print("Votre rendu monnaie est de", rendu, "euros.")
    else:
        print("Impossible\nVous n'avez pas mis assez d'argent pour acheter cette boisson.")
        conditions = False

