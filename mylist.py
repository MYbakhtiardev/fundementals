fruits = ["apple", "orange", "mango", "banana"]

fruits.append("lemon")
print(fruits)

fruits.extend(["rambutan", "pineapple"])
print(fruits)

fruits.remove("rambutan") #only remove the first one
print(fruits)

fruits = fruits + ["rambutan", "pineapple"]
print(fruits)

fruits[1] = "berry"

pineapple_count = fruits.count("pineapple")
print(pineapple_count)

del fruits[7]
print(fruits)

fruits.clear() #clear the entire list
print(fruits) #this will print an empty list

del fruits #delete the entire list
# print(fruits) #this will throw an error

fruits = ["apple", "orange", "mango", "banana", "apple", "apple"]
print(fruits.count("apple"))
print(fruits.index("apple"))

uppercase = [item.upper() for item in fruits]
print(uppercase)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

imported_fruits = fruits

importedfruits = [item for item in fruits]

importedfruits2 = fruits.copy()

import copy
importedfruits2 = copy.deepcopy(fruits)