def describe_city(city, country="Iceland"):
    print(city, "is in", country)

for i in range(3):
    city = input("Entrez le nom d'une ville : ")
    country = input("Le pays par défaut est Iceland.")

    if country == "":
        describe_city(city)
    else:
        describe_city(city, country)
