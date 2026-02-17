
try:
    no1=int(input("Enter the first number: "))
    no2=int(input("Enter the second number: "))
    result=no1/no2
    print("The result is: ", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
else:
    print("Division performed successfully.")
finally:
    print("Thank you for using the safe division program.")
    