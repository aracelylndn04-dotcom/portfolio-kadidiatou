a = " Levez-vous vite, orages désirés qui devez emporter rené dans les espaces d'une autre vie !"
b = ""
for i in range(len(a)):
    if a[i]=="e" or a[i]=="é" or a[i]=="è" or a[i]=="ê":
        b +="a"
    else:
        b +=a[i]
print(b)