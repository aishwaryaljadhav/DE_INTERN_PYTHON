try:
    a=int(input("Enter the size of list: "))
    lst=[]
    for i in range(a):
        num=int(input("Enter the number: "))
        lst.append(num)
    index=int(input("Enter the index to access: "))
    print("The element at index", index, "is:", lst[index])
except IndexError:
    print("Error: Index out of range. Please enter a valid index.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
else:
    print("Element accessed successfully.")
finally:
    print(" Program Completed.")
