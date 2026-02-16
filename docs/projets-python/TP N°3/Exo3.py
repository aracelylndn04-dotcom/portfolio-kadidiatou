mois=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print("Saissisez un mois de l'année de 2024,")
print("la saisit doit se faire en répresentant le mois en chiffre,")
num=int(input("Choississez alors entre 1 à 12 : "))
if num<=12 and num>=1 :
    nbr_jours= mois[num-1]
    print("Le nombre de ce jours pour ce mois est :",nbr_jours)
else :
    print("Veuillez svp choisir entre 1 à 12: ")



