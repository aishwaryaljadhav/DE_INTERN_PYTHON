def square(num):
    return num ** 2
def cube(num):
    return num ** 3
def operate(num, operation):
    return operation(num)
result=operate(3, square)
print(result) 