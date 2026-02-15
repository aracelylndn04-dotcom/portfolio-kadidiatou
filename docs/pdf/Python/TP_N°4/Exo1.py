somme_euro=float(input("Entrez une somme en euros : "))
dollars =1.8
somme =(somme_euro*dollars)
print("La somme en dollars est :",somme,"dollars.")
message = input("Tapez stop pour arreter ou go pour continuer").lower()
print(message)
while message=="go":
    somme_euro=float(input("Entrez une somme en euros : "))
    dollars =1.8
    somme =(somme_euro*dollars)
    print("La somme en dollars est :",somme,"dollars.")
    message = input("Tapez stop pour arreter ou go pour continuer").lower()
    print(message)