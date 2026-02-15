
print("Choisissez une option :")
print("1 pour Convertir de Celsius en Fahrenheit")
print("2 pour Convertir de Fahrenheit en Celsius")
choix = input("Entrez 1 ou 2 : ")

if choix == "1":
    celsius = float(input("Entrez la température en Celsius : "))
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit, "°F")
elif choix == "2":
    fahrenheit = float(input("Entrez la température en Fahrenheit : "))
    celsius = (fahrenheit - 32) * 5/9
    print(celsius, "°C")
else:
    print("Option invalide. Veuillez entrer 1 ou 2.")
