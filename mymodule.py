def add(a,b):
    print("The sum of", a, "and", b, "is:", a+b)
    return a+b

def subtract(a,b):
    print("The difference between", a, "and", b, "is:", a-b)
    return a-b
def multiply(a,b):
    print("The product of", a, "and", b, "is:", a*b)
    return a*b
def divide(a,b):
    if b!=0:
        return (f"The quotient of {a} and {b} is: {a/b}")
    else:
        return ("Error: Division by zero is not allowed.")
  
