# dicionary Basics

student = {
    "name": "Gautam kumar",
    "city": "Muzaffarpur",
    "age": 19,
    "Roll no":33,
}

print(type(student))
print(student)
print(student["name"])
print(student["Roll no"])
student["city"]= "Banglore"
print(student) #city is updated
student["favSub"]= "Mathematics"
print(student) #favSub is added
student.pop("favSub")
print(student) #favSub is removed

print(student.keys())
print(student.items())
