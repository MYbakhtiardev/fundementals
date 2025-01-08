#read only list
fruits = ["apple", "orange", "mango"]
print(fruits)
fruits[0] = "banana"
print(fruits)

#tuple
coordinates = (1, 2, 3)
print(coordinates)
print(coordinates[0])

#2d tuple
tuple2d = ((1, 2, 3), (4, 5, 6))
print(tuple2d)

mydict = {("x","y"):10}
print(mydict)
print(mydict[("x","y")])

fruits = ["apple", "orange", "mango"]
newfruits = fruits
print(newfruits)
fruits[0] = "banana"
print(newfruits) #it will print the new list as it find address for fruits
newnewfruits = fruits.copy()
print(newnewfruits)
fruits[0] = "lemon"
print(newnewfruits)

x = "apples", "oranges", "grapes"
print(x)
print(type(x)) #tuple

#tuple in list
fruits = ["apples", "oranges", "grapes"]
fruits[2] = "banana", "lemon" #default is tuple
print(fruits)
print(fruits[2][1]) #lemon
print(fruits[0][1]) #apples (p)
print(type(fruits[0]))

#single item tuple
fruits = ("apple",) #tuple has comma ,
print(fruits[0])
print(type(fruits))

#empty tuple
fruits = ()
print(fruits)
print(type(fruits))