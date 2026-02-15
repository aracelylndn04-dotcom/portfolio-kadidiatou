note = [7,18,7,5,10,13]
note.append(12)
print(note)
moyenne = sum(note) / len(note)
print("Note minimale :", min(note))
print("Note maximale :", max(note))
note.remove(10)
note.sort()
print(note)
note.sort(reverse=True)
print(note)







