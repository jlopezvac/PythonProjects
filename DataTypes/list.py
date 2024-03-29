# lists
my_list = ["Fender", "Warwick", "Epiphone", "Yamaha", "Cort", "Jackson"]

# print the number of items
print(len(my_list))

# print all
print(my_list)

# print the first element
print(my_list[0])

# print the last element
print(my_list[-1])

# print a range
print(my_list[2:5])
print(my_list[:3])
print(my_list[2:])
print(my_list[1:-1])

# add item
my_list.append("LTD")

# iterate
for value in my_list:
    print(value)