km=int(input("Enter the distance of kilometers"))
ratio = 0.621371
mi = km * ratio 
print("The entered value in miles:",mi)

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    snum = num1
elif(num2 >= num1) and (num2 >= num3):
    snum = num2
else:
    snum = num3
print("The big among number is ",num1, ",", num2, "and", num3, "is: ", snum)
