no1=int(input("Enter first number: "))
no2=int(input("Enter second number: "))
no3=int(input("Enter third number: "))
print ("The numbers are: ", no1, no2, no3)
if (no1>no2 and no1>no3):
    print("The greatest number is: ", no1)
elif (no2>no3):
    print("The greatest number is: ", no2)
else:
    print("The greatest number is: ", no3)