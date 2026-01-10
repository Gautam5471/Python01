# Methods in list

#indexing

# lists are mutable/changable
marks = [100,99,97,95,90]
print(marks)

# marks[1]=98
# print(marks)

# slicing
print(marks[1:3])


print(max(marks))
print(min(marks))

marks.append(92)
print(marks)
marks.sort()
print(marks)
marks.pop(0)
print(marks)
marks.remove(100)
print(marks)
marks.insert(0,100)
print(marks)


# # string are immutable
# name = "Gautam"
# name[0]="g"
# print(name[0])