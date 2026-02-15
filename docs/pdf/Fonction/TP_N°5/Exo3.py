def mode_semaine(heure:float):
    if heure>=6 and heure<=9 or heure>=17 and heure<=22:
        mode = "Confort"
    else:
        mode = "Eco"
    return mode

def mode_weekends(heure: float):
    assert(heure>=0 and heure<24)
    if heure < 9 :
        mode ="Eco"
    elif heure < 22:
        mode = "Confort"
    else:
        mode = "Eco"
    return mode

def mode(jour: str, heure:int):
    if jour == "Samedi" or jour == "Dimanche":
        return mode_weekends(heure)
    else:
        return mode_semaine(heure)
print(mode("Lundi",23))
print(mode("Mardi",13))
print(mode("Dimanche",17))
print(mode("jeudi",21))
print(mode("Samedi",9))