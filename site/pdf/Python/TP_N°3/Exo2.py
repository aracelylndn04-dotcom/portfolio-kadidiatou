Temperature = int(input("Saissisez un chiffre en dégrés celsius: "))
if Temperature<=00 :
    print("Le temps est glacial.")
elif Temperature >=1 and Temperature<=20 :
    print("Il fait froid.")
elif Temperature>=21 and Temperature<=40 :
    print("Il fait chaud.")
else :
    print("Il fait très chaud.")
