age=int(input("Tapez votre age :"))
infos=(input("Etes vous un étudient(e) ou pas ? oui ou non? "))
gratuit=00
tarif=17
demi_tafif=tarif/2
if age<=5 :
    print("Le prix de ton billet est :",gratuit,"euro, donc gratuit.")
elif age<=16 or age>=65 or infos=="oui":
    print("Le prix de ton billet est :",demi_tafif,"euro.")
else :
    print("Le prix de votre biellet est :",tarif,"euro.")


