le_quota = 30
jours_de_conges= int(input("Combien de jours de congé veux-tu prendre ? "))
if jours_de_conges > le_quota:
    print("Le nombre de jours démandés n'est pas autorisés! Le Quota disponible est de",le_quota,"jours.")
else:
    print("Congé accordé pour",jours_de_conges, "jours.")
