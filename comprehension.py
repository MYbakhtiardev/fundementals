fruits = ["apple", "orange", "mango", "rambutan", "durian"]
#result = [5,,6,5,8,6]

result = [len(fruit) for fruit in fruits]
print(result)

#orrr
result = []
for fruit in fruits:
    result.append(len(fruit))
print(result)


prices = [10, 20, 30, 40, 50]
#find prices with tax of 0.6

result = [(price + (price * 0.06)) for price in prices]
print(result)

#orrr
result = []
for price in prices:
    result.append(price + (price * 0.06))
print(result)

celcius_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#in fahrenheit

fahrenheit_values = [(celcius_value * (9/5) + 32) for celcius_value in celcius_values]
print(fahrenheit_values)

#orrr
fahrenheit_values = []
for celcius_value in celcius_values:
    fahrenheit_values.append((celcius_value * (9/5) + 32))
print(fahrenheit_values)

given_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#remove even number from the list

result = [number for number in given_number if number % 2 != 0]
print(result)
print()

#shallow copy
fruits = ["apple", "orange", "mango", "rambutan", "durian"]
new_shallow_fruits = fruits
print("Before fruits", fruits)
print("After new_shallow_fruits", new_shallow_fruits)

fruits[1] = "banana"
print("Before fruits", fruits)
print("After new_shallow_fruits", new_shallow_fruits)
print()

#deep copy
fruits = ["apple", "orange", "mango", "rambutan", "durian"]
new_deep_fruits = fruits.copy()
print("Before fruits", fruits)
print("After deep_fruits", new_deep_fruits)

fruits[1] = "banana"
print("Before fruits", fruits)
print("After deep_fruits", new_deep_fruits)



