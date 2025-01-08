#2 loops, while loop and for loop

fruits = ["apple", "orange", "mango", "banana", "lemon", "pen", "pineapple"]
print(fruits)
for fruit in fruits:
    # print(fruit)
    print(fruit, fruits.index(fruit)) #or print(fruit, index) index = index + 1

#orrrrr
for index in range(len(fruits)):
    print(fruits[index], index)

#orrr
enumerate_fruits = enumerate(fruits)
print(enumerate_fruits)
print(list(enumerate_fruits)) #enumerate is iterable object so it can be converted to list

#orrrr
for index, fruit in enumerate(fruits):
    print(fruit, index)

fruits = ["apple", "orange", "mango", "banana"]
colours = ["red", "orange", "green", "yellow"]
taste = ["sweet", "sour", "sour", "bitter"]

zipper = zip(fruits, colours, taste)
print(list(zipper))

sports = ["cricket", "football", "tennis", "badminton"]
for sport in sports:
    print(sport)
else:
    print("No more sports")

searched_sports = "tennis"
for sport in sports:
    print(sport)
    if sport == searched_sports:
        print("Found at index", sports.index(sport))
        break
else:
    print("Sports is not found")

multi = 6
for i in range(1, 11):
    if i == 5:
        continue #continue is used to skip the current iteration
    print(multi, "x", i, "=", multi * i)


#while loop
i = 1
while i <= 10:
    # print(i)
    i += 1
else: #else is optional, it is executed when the condition is false
    print("")
print("statement is executed")

result = 0
given_number = 98765431
while(given_number != 0):
    remainder = given_number % 10
    result = result * 10 + remainder
    given_number = given_number // 10
    if given_number == 98:
        print("result is", result)
        break
else:
    print(result)