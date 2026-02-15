def testVoyelle(test:str):
    voyelle =["i","u","o","a","e","é","è","ê","y"]
    if test in voyelle:
        return True
    else:
        return False
    
print(testVoyelle("a"))
print(testVoyelle("b"))
print(testVoyelle("e"))
print(testVoyelle("f"))

def compteVoyelle(chaine:str):
    testVoyelle()
    texte = input("Entrez une phrase : ")
    resultat = compteVoyelle(texte)
    print("Nombre de voyelles :", resultat)
    
compteVoyelle()