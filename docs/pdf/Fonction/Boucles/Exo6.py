A = "Héautontimorouméros"
B = ""
for i in range(len(A)):
    if (i %2==0):
        B += A[i]
    else:
        B +="*"
    print(i)
    print(B)
print(B)