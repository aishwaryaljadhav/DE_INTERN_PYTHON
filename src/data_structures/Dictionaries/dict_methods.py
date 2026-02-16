dict={"name": "Aishwarya", 
      "age": 21, 
      "marks": {"phy": 85, "chem": 90, "bio": 95}, 
      "edu": "BTech-CSE"}
print(dict["marks"]["chem"])
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("name"))
dict.update({"age": 22})
print(dict)