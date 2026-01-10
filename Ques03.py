# #Ask the user for their 3 favorite movies and store them in a list.

# Favmovies1 = input ("Enter the  first favorite movies name :")
# Favmovies2 = input ("Enter the  second favorite movies name :")
# Favmovies3 = input ("Enter the  third favorite movies name :")

# movies = [Favmovies1, Favmovies2, Favmovies3 ]
# print(movies)


#Create a tuple of marks (87, 64, 33, 95, 76) and print the highest and lowest marks using max() and min().

tuple = (87, 64, 33, 95, 76)
print("maximum marks is ",max(tuple))
print("minimum marks is ",min(tuple))



# Write a program to check grade based on marks (A/B/C/D) using if-elif-else.

marks = int(input ("Enter your marks :"))
if(marks>=90 and marks<=100):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
elif(marks>=60 and marks<=70):
    print("D")
elif(marks>=0 and marks<60):
    print("Fail")


