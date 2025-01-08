import os

print("Shopping") #string
print(10) #integer
print(1445.75) #float
print(True) #boolean
print(type(10)) #type_check
person = {"name":"John", "age":36} 
print( person )#dictionary
print({"pizza", "cola", "chocolate"}) #set
arr = ["apple", "banana", "cherry"]
print(arr) #list
print(["python", "java", "c++", 1, 2, 3])
#list can have different data types
print("tv", 1, 1.2, True) #tuple
print(f"Hello{os.linesep}World") #f-string os.linesep
pi = 3.14159
print(f"Pi rounded to two decimal places: {pi:.2f}") #f-string use when dynamic string

nums = [1, 2, 3, 4, 5]
x = 5
total0 = nums[0] + x
print(total0)

#packing and unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates
print(x, y, z)

print(1, 2, 3, 4, 5, sep=" | ") #separator
print(1, 2, 3, 4, 5, sep=" | ", end=" | ") #separator

# Sunday morning we ask computer
# Where are you going ?
# To output we use "print" function
# print is a built in function
# To call a built in function we use "()" after the function name
# What is built in function
# buyLunch is a built in function among humans
# print is a function in python
print("Shopping") # arguments are passed between ()

# Problem 1
# buyLunch("nasi", "ayam", "sirap")
# BuyLunch buyLunch or BuyLunch are totally different for Computers
# We have a term "case sensitive"

# Problem 2
# buyLunch["nasi", "ayam", "siram"]
# I cannot use [] instead of ()
# the meaning for [] is different from ()
# You must follow the programming language "syntax" while creating the statement

# What you going to buy ?
print("Television")
# How many ?
print(10)
# How much ?
print(1445.75)
# Is it Available in the shop ?
print(True)

# What are the values / literals the computer actually print ?
# "Shopping", "Television", 10, 1445.75, True
# String Type: "Shopping", "Television" (String Literals)
# String Literals are always encloded with double quote ""
# Number Type: 10, 1455.75
# 10 is an integer literal where there is no decimal values
# 1455.75 is a float literal which has decimal values
# Both Integer Literal and Float Literal are not enclosed with double quote ""
# Boolean Type: True / False
# True is a boolean Literal (T is capital)
# False is another boolean Literal (F is capital)
# True also using alphabets why it is not enclosed with double quote ""
# True / False is a keyword in python
# Keywords are building blocks in any programming language

# Monday Evening computer is leaving our house
# Where are you going
print("Fruits Shop")
# What are you going to buy ?
# When ever you have more than one value use a box []
# the box is called "list" in python
# the items inside the box are seperated by comma
print(["apple", "orange", "mango"])
# How many are you going to buy ?
print([5, 10, 2])
# How much are they ?
print([1.20, 0.80, 4.60])
# Are they available in the shop ?
print([True, False, True])
# Who came to our shop ?
print("1 Customer")
# Who is that ?
print(["Khairi Bin Abu Bakar", 720102121234, 1255.25, "Radio", 1, 623.45])

# In other programming languages we cannot put data of different types
# into a single box. They are called "homogeneous" list
# However in python we can put data of different types
# into a single box. So it is called "heterogeneous" list


# In python the built in function print has many features
# the print function takes any number of arguments
# where are you going ?
print("Shopping", "Cinema") # now you are passing 2 arguments to the print function
# the arguments are seperated by comma
# However the output does not have comma
# What are you going to buy ?
print("Television", ["apple", "orange", "mango"]) # again we are passing 2 arguments
# the first one is string and second one is list of strings
# the output does not have comman but to differentiate the items inside the list 
# the comma still appears
print("Television", 10, 1455.55, True) # we are passing 4 arguments to print function

# Sunday morning we ask computer
# Where are you going ?
# To output we use "print" function
# print is a built in function
# To call a built in function we use "()" after the function name
# What is built in function
# buyLunch is a built in function among humans
# print is a function in python
print("Shopping") # arguments are passed between ()

# Problem 1
# buyLunch("nasi", "ayam", "sirap")
# BuyLunch buyLunch or BuyLunch are totally different for Computers
# We have a term "case sensitive"

# Problem 2
# buyLunch["nasi", "ayam", "siram"]
# I cannot use [] instead of ()
# the meaning for [] is different from ()
# You must follow the programming language "syntax" while creating the statement

# What you going to buy ?
print("Television")
# How many ?
print(10)
# How much ?
print(1445.75)
# Is it Available in the shop ?
print(True)

# What are the values / literals the computer actually print ?
# "Shopping", "Television", 10, 1445.75, True
# String Type: "Shopping", "Television" (String Literals)
# String Literals are always encloded with double quote ""
# Number Type: 10, 1455.75
# 10 is an integer literal where there is no decimal values
# 1455.75 is a float literal which has decimal values
# Both Integer Literal and Float Literal are not enclosed with double quote ""
# Boolean Type: True / False
# True is a boolean Literal (T is capital)
# False is another boolean Literal (F is capital)
# True also using alphabets why it is not enclosed with double quote ""
# True / False is a keyword in python
# Keywords are building blocks in any programming language

# Monday Evening computer is leaving our house
# Where are you going
print("Fruits Shop")
# What are you going to buy ?
# When ever you have more than one value use a box []
# the box is called "list" in python
# the items inside the box are seperated by comma
print(["apple", "orange", "mango"])
# How many are you going to buy ?
print([5, 10, 2])
# How much are they ?
print([1.20, 0.80, 4.60])
# Are they available in the shop ?
print([True, False, True])
# Who came to our shop ?
print("1 Customer")
# Who is that ?
print(["Khairi Bin Abu Bakar", 720102121234, 1255.25, "Radio", 1, 623.45])

# In other programming languages we cannot put data of different types
# into a single box. They are called "homogeneous" list
# However in python we can put data of different types
# into a single box. So it is called "heterogeneous" list


# In python the built in function print has many features
# the print function takes any number of arguments
# where are you going ?
print("Shopping", "Cinema") # now you are passing 2 arguments to the print function
# the arguments are seperated by comma
# However the output does not have comma
# What are you going to buy ?
print("Television", ["apple", "orange", "mango"]) # again we are passing 2 arguments
# the first one is string and second one is list of strings
# the output does not have comman but to differentiate the items inside the list 
# the comma still appears
print("Television", 10, 1455.55, True) # we are passing 4 arguments to print function

# Questions
print("Television", 10, "RM", 1455.55, True) # you will have a space 
# "RM" is string literal 1455.55 is float literal

print("Television", 10, "RM1455.55", True) # you won't have space
# RM1455.55 is string literal

# When it prints string we do not have double quote printed
# When it prints the items inside the list which is string then it prints single quote
print("Television", ["apple", "orange"])
# The string literal can be enclosed with double quote "" or single quote ''
# print function convert the entire list into a string and print it
# "['apple', 'orange']"

# packing / unpacking / iterating
# putting the balls inside the box = packing
# throwing the balls from the box = unpacking
# pulling out the balls one by one from the box = iterating

# I want to know the total amount to be paid when i buy
# 10 TVs and each cost me 1455.55
print("Price of", 10, "TVs", "RM", 10 * 1455.55)






