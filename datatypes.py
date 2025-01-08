x = 10
print(type(x))

y = "Letter"
print(type(y))

z = True
print(type(z))

a = [1, 2, 3]
print(type(a))

b = (1, 2, 3)
print(type(b))

c = {1, 2, 3}
print(type(c))

d = {"name": "John", "age": 36}
print(type(d))

e = None
print(type(e))

f = lambda x: x + 10
print(type(f))

g = 1 + 2j
print(type(g))

h = b"Hello"
print(type(h))

i = bytearray(5)
print(type(i))

j = memoryview(bytes(5))
print(type(j))

k = range(6)
print(type(k))

l = frozenset({1, 2, 3})
print(type(l))

m = slice(6)
print(type(m))

n = object()
print(type(n))

o = set()
print(type(o))


#exe

test1 = 10
test2 = "Letter"
# this is error answer = test1 + test2

answer = str(test1) + test2
print(answer)

test3 = "A16"
#answer = int(test3) + test1 nuh uh
answer = int(test3, 16) + test1
print(answer)

test4 = "" #bool is false or 0
test5 = " " #bool is true or non-0
answer = bool(test4)
print(answer)
answer = bool(test5)
print(answer)
#bool is also a number 0 or 1 meaning int() will return 0 or 1

#list of type casting (str, int, float, bool, list, tuple, set, dict, bytearray, bytes, memoryview, range, frozenset, slice, object)

# When the value 10 is assigned to the variable x
# the variable x is automatically assigned with a data type
# called integer by python
x = 10
# How can i know what is the data type assigned to this variable ?
# you can use the built in function "type"
print(type(x))

# When the value 1455.55 is assigned to the variable y
# the variable y is automatically assigned with a data type
# called float by python
y = 1455.55
print(type(y))

# When the value True is assigned to the variable z
# the variable z is automatically assigned with a data type
# called bool by python
z = True
print(type(z))

# When the value Welcome to Python is assigned to the variable message
# the variable message is automatically assigned with a data type
# called str by python
message = "Welcome to Python"
print(type(message))

x = 150
y = 100
z = 1455.55
result = x + y # addition since both sides of the + are integers
print(result)
result = x + z # addition since one side of the + is integer and another side is float
print(result)
# integer and fload comes under number category

# I have a number 
carnumber = 6428
carplate = "XYZ"
# carplatenumber = carplate + carnumber 

# error once side of + is integer another side of + is string
# When python see + operator and one side of the + is string
# python will immediately try to concatenation rather than addition
# for concatenation both side of + must be string
# since we have integer at one side python throws error immediately
# the value "XYZ" cannot be converted into a number
# but the value 6428 can be converted to a string
# How can we convert number to a string ?
# you can use a built in function str
carplatenumber = carplate + str(carnumber)
print(carplatenumber)
# Note: The process of converting from one data type to another data type 
# is called "type casting"

x = "101"
y = 5
# result = x + y
# however in this case we can convert "101" to 101
# you can use built in function int to convert string to integer
result = int(x) + y # int function assumes the string is having a decimal value
print(result)

x = "A101" # this is a hexadecimal value
y = 5
# result = x + y
# however in this case we can convert "A101" to 41217
# you can use built in function int to convert string to integer
# to tell the int function that we have hexadecimal value in the variable
# we have to use base 16 
result = int(x, 16) + y 
print(result)

x = "1455.55"
y = 10
# however in this case we can convert "1455.55" to 1455.55
# you can use built in function float to convert string to float
result = float(x) * y
print(result)

# bool function helps you to convert a literal to boolen value
# as long as the literal is a number other than 0 it is True
x = 5
print(bool(x))
# as long as the literal is a number and equals to 0 it is False
x = 0
print(bool(x))
# as long as the literal is a string other than "" it is True
x = "Hello"
print(bool(x))
# as long as the literal is a string and equals to "" it is False
x = ""
print(bool(x))

x = True
y = "Hello"
result = str(x) + y # str(x) returns True
print(result)
result = str(int(x)) + y # int(x) returns 1 if True or 0 if False
print(result)

# if you want to convert x = "True"
x = str(x)
x = "" # empty string
x = " " # string with space
# how do we teach alphabets to computers ??
# In computers A, B, C...... everything has a value (number)
# which is calles ASCII values
print("6") # 54
print(6) # 6
# this is the reason why we need int function to convert "6" to 6
# that is why converting "6" to 6 or 6 to "6" is also called typecasting