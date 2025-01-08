fruits = ["apple", "orange", "mango"]
# print(fruits[1])

#length of the list
print(len(fruits))

for item in fruits:
    print(item)

# from last item
for item in fruits[::-1]:
    print(item)

print(fruits[-1]) #last item in the list
print(fruits[-2]) #second last item

print(fruits[1:3]) #start from index 1 to index 2
print(fruits[1:]) #start from index 1 to the end
print(fruits[:3]) #start from the beginning to index 2
print(fruits[0:2:3]) #start from index 0 to index 2 with step of 2

#append (add an item to the list)
fruits.append("banana")
print(fruits)

#remove (remove the item from the list)
fruits.remove("apple")
print(fruits)

#pop (remove last item from the list)
fruits.pop(1)
print(fruits)

#insert (insert an item to the list)
fruits.insert(1, "watermelon")
print(fruits)

#copy (copy the list)
fruits_copy = fruits.copy()
print(fruits_copy)

#count (count the number of items in the list)
print(fruits.count("apple"))

#sort (sort the list)
fruits.sort()
print(fruits)

#reverse (reverse the list)
fruits.reverse()
print(fruits)

#extend (extend the list)
fruits.extend(["apple2", "orange2", "mango2"])
print(fruits)

#clear (remove all items from the list)
fruits.clear()
print(fruits)

salary = [1000, 2000, 3000, 4000, 5000]
average = sum(salary) / len(salary)
print(average)

#2d list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][1]) #5

# for row in matrix:
#     for item in row:
#         print(item)

#remove an item from the 2d list
matrix[1].remove(5)
print(matrix)

#add an item to the 2d list
matrix[1].append(10)
print(matrix)

person = [ "John", 36, "New York" ]
name, age, city = person
print(name, age, city)

student = [
    ["Love", 12, "US"],
    ["New York", 12345]
]

name, age, city = student[0]
print(name, age, city)
residence, zipcode = student[1]
print(residence, zipcode)
print(student[1:])

x = y = z = [1, 2, 3]
print(x, y, z)

