
liste=["urgent","important","à faire"]
phrase=input("Tapez une phrease contenant au moins ces 3 mot : urgent,imporatnt,à faire.")
mot1= "urgent"
mot2="important"
mot3="à faire"
if mot1 in phrase :
    print("Principe validée")
elif mot2 in phrase :
    print("Principe validée")
elif mot3 in phrase :
    print("Principe validée")
else :
    print("Principe non validée")