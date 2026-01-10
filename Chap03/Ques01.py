# write a program that takes your favorite color name as a input and prints
# middle 3 character
# kast 2 character

#white


str = input("enter the favorite color : "+"\n")
print(len(str))
mid = len(str)//2 #  "//" remove the decimial part 
print(mid)
print(str[mid-1:mid+2])
print(str[-2:]) #negative indexing


