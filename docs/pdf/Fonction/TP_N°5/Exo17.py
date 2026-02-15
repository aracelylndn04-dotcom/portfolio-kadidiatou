def mention(note):
    if 0 <= note < 10:
        print("éliminé")
    elif 10 <= note < 12:
        print("Passable")
    elif 12 <= note < 14:
        return "AB"
    elif 14 <= note < 16:
        print("B")
    elif 16 <= note < 20:
        print("TB")
    else:
        print("Note invalide")
mention(8)
mention(15)
mention(14)
mention(22)
