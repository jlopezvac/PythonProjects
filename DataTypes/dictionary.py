my_ditcionary = {"Iron Maiden" : "United Kingdon", "Hammerfall" : "Sweden", "Edguy" : "Germany",
    "Sonata Arctica" : "Finland", "Testament" : "USA", "Kreator" : "Germany"}

# print the number of items
print(len(my_ditcionary))

# print the dictionary
print(my_ditcionary)

# print keys
print(my_ditcionary.keys())

# print values
print(my_ditcionary.values())

# print the first element
print(list(my_ditcionary.items())[0])

# add item
my_ditcionary["977"] = "Spain"
print(my_ditcionary)

# iterate items
for key, value in my_ditcionary.items():
    print("The bant", key, "is from", value)

