montant = float(input("Entrez le montant de votre achat : "))
if montant <= 50:
    points = 0
    print("Vous n'avez pas gagné de point(s) de fidélité.")
    print("Merci pour votre achat !")
elif montant >50 and montant<= 100:
    points = (montant / 10)
    print("Vous avez gagné", points, "point(s) de fidélité.")
    print("Bravo ! Continuez ainsi.")
else:
    points = (montant / 5) 
    print("Vous avez gagné", points, "point(s) de fidélité.")
    print("Félicitations ! Vous êtes un client fidèle.")
