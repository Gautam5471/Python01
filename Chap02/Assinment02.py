#Write a program that takes number of frietotal bill amount and nds as input. Calculate how much each person will pay. 
 #Also print the data type of each variable used.

Numoffriend = int(input("enter the number of friend is : "))
TotalBillAmount = 2000

HowmuchPay = TotalBillAmount / Numoffriend

print("how much pay by each friends is : ",HowmuchPay)
print(type(Numoffriend ))
print(type(TotalBillAmount ))
print(type(HowmuchPay ))

