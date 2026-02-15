notes = [8,9,10]
def avg(notes):
    assert len(notes) >0
    return sum(notes) / len(notes)
print(avg(notes))

notes_empty=[]
print(avg(notes_empty))