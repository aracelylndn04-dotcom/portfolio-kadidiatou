import random
print("1.Addition\n2.Multiplication.")
choix = int(input("Entrez 1 ou 2 pour effectuer votre choix : "))
def addition():
    un = random.randint(5,20)
    deux = random.randint(5,20)
    print(un,"et",deux)
    reponse1 = int(input("Entrez le résulat de l'addition de ces deux nombres : "))
    solution1 = int(un + deux)
    print("La solution est :",solution1)
    verification(reponse1,solution1)
def multiplication():
    num1 = random.randint(30,50)
    num2 = random.randint(1,20)
    print(num1,"et",num2)
    reponse2 = int(input("Entrez le résulat de la multiplication de ces deux nombres : "))
    solution2 = int(num1*num2)
    print("La solution est :",solution2)
    verification(reponse2,solution2)
def verification(reponse:int, solution:int):
    if reponse==solution:
        print("Votre réponse est correct.")
    else:
        print("Votre réponse est incorrect.")
if choix ==1:
    addition()
elif choix == 2:
    multiplication()
else:
    print("Erreur veuillez bien revoir votre saisit!!")