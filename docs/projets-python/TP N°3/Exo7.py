phrase = input("Saisis une phrase : ")
longueur = len(phrase)
if longueur <=10:
    print("Phrase très courte.")
elif longueur <=30:
    print("Phrase de longueur moyenne.")
else:
    print("Phrase assez longue.")

