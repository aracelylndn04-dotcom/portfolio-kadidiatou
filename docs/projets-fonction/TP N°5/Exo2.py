import random
def lancer_de_des(nbr_des_a_lance:int,nbr_faces_des:int):
    resultat=""
    print(nbr_des_a_lance,"et",nbr_faces_des)
    for i in range(nbr_des_a_lance):
        de=random.randint(1,6)
        resultat+=" "+str(de)
    print(resultat)
lancer_de_des(2,10)