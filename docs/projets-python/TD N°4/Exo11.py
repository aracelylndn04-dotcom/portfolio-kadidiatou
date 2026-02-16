import random
B=random.randint (1,100)
A= int(input("Devinez le nombre choisit entre 1 à 100 :"))
print ("Le  nombre à dévinez était:",B)
chance=7
while A != B and chance>=0:
    if A<B :
        chance=chance-1
        print("Trop petit")
    elif A>B :
        chance=chance-1
        print("Trop grand")
    print("Il vous reste", chance, "chance")
    A=int(input("Reponse"))

if chance==0:
    print("Perdu")
if A==B :
    print("Wow vous avez dévinez le bon nombre!!!")



