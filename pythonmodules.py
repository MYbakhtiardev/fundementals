import os
if not os.path.exists("demo"):
    os.mkdir("demo")
    os.chdir("demo")
    f = open("class01.txt", "w")
    f.write("This is incredible!!!This is incredible 2!!!")
    f.close()

total = 0
mynumbers = [10, 20, 30, 40, 50]
for number in mynumbers:
    total = total + number
print(total)

from functools import reduce
def calculateTotal(x, y):
    return x + y
result = reduce(calculateTotal, mynumbers)
print(result)

from itertools import permutations, combinations
print(list(permutations([1, 2, 3], 2))) #2 is the number of elements in the tuple
print(list(combinations([1, 2, 3], 2)))
