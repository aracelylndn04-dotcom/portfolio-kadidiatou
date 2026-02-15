age=int(input("Tapez votre age :"))
if age<=12 :
    print("Enfant.")
elif age>12 and age<=17 :
    print("Adolescent.")
elif age>=18 and age<=64:
    print("Adulte.")
elif age>=65 :
    print("Senior.")
else :
    print("Impossible.")



