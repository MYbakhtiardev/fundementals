def total(data):
    # pass #keyword to pass the function
    result = 0
    for item in data:
        result += item
    return result

def total2(data):
    return sum(data), len(data)

result,abc = total2([1, 2, 3, 4, 5])
print(result)

print(total2([1, 2, 3, 4, 5]))

#variable length argument (* args). it will take any number of arguments and store them in a tuple
def calculateTotal(*data):
    result = 0
    for item in data:
        result += item
    return result

print(calculateTotal(1, 2, 3, 4, 5))
print(calculateTotal(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

data = [1, 2, 3, 4, 5]
print(calculateTotal(*data)) # * is unpacking the list into a tuple

x = [10, 20, 30]
y = [40, 50, 60]
print(x, y)
print(*x, *y) 


print(list(zip([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4])))

print(all([True, True, True]))

print(list(enumerate(["apple", "orange", "mango"], start=25)))
