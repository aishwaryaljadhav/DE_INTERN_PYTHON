marks={}
x=int(input("Enter phy marks: "))
y=int(input("Enter chem marks: "))
z=int(input("Enter math marks: "))
marks.update({"phy": x})
marks.update({"chem": y})
marks.update({"math": z})
print(marks)