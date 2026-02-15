
ok = False
while ok == False :
    entier=int(input("saissisez un entier"))
    print(isinstance(entier,int))
    if isinstance(entier,int):
        print(entier)
        ok == True
