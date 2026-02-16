# with open("practise.txt", "w") as f:
#     f.write("This is a practise file.\n")
#     f.write("We are learning file handling in Python.\n")

with open("practise.txt", "r") as f:
    data = f.read()

new_data=data.replace("practise", "practice")
print(new_data)

with open("practise.txt", "w") as f:
    f.write(new_data)