myTuple = (78,90,75)
studentTuple = ("Gautam","S.A","kunal","prakhar","Gautam")


# studentTuple[0]="hello" # tuples are immutable/ not changable

print(studentTuple[2])


#empty Tubples
emptyTuples =()
singleTuple =(1,)
print(type (singleTuple))
print(type (emptyTuples))
print(type (studentTuple))

print(studentTuple.index("Gautam"))
print(studentTuple.count("Gautam"))
print(studentTuple.count("S.A"))