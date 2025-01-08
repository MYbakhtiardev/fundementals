product = "television"
price = 100
discount = 0.1
total = price * (1 - discount)
print(f"The total price of {product} is {total}")

x = 10
print(x)
print(id(x)) #decimal
print(hex(id(x))) #hexadecimal

x = 11
print(x)
print(id(x)) #decimal
print(hex(id(x))) #hexadecimal

y = 10
print(y)
print(id(y)) #decimal (same as x as it is the same value)
print(hex(id(y))) #hexadecimal

x = "hello"
print(x)
print(id(x)) #decimal
print(hex(id(x))) #hexadecimal

#is keyword
x = 10
y = 10
print("X is y ",x is y) # is is to check if the value is the same or not by comparing the address location

# Sunday morning we ask computer
# Where are you going ?
# To output we use "print" function
# print is a built in function
# To call a built in function we use "()" after the function name
# What is built in function# buyLunch is a built in function among humans
# print is a function in pythonprint("Shopping") 
# arguments are passed between ()
# Problem 1
# buyLunch("nasi", "ayam", "sirap")
# BuyLunch buyLunch or BuyLunch are totally different for Computers
# We have a term "case sensitive"
# Problem 2
# buyLunch["nasi", "ayam", "siram"]
# I cannot use [] instead of ()
# the meaning for [] is different from ()
# You must follow the programming language "syntax" while creating the statement
# What you going to buy ?print("Television")
# How many ?print(10)
# How much ?print(1445.75)
# Is it Available in the shop ?print(True)
# What are the values / literals the computer actually print ?
# "Shopping", "Television", 10, 1445.75, True
# String Type: "Shopping", "Television" (String Literals)
# String Literals are always encloded with double quote ""
# Number Type: 10, 1455.75
# 10 is an integer literal where there is no decimal values
# 1455.75 is a float literal which has decimal values
# Both Integer Literal and Float Literal are not enclosed with double quote ""
# Boolean Type: True / False# True is a boolean Literal (T is capital)
# False is another boolean Literal (F is capital)
# True also using alphabets why it is not enclosed with double quote ""
# True / False is a keyword in python
# Keywords are building blocks in any programming language
# Monday Evening computer is leaving our house
# Where are you goingprint("Fruits Shop")
# What are you going to buy ?
# When ever you have more than one value use a box []
# the box is called "list" in python
# the items inside the box are seperated by commaprint(["apple", "orange", "mango"])
# How many are you going to buy ?print([5, 10, 2])
# How much are they ?print([1.20, 0.80, 4.60])
# Are they available in the shop ?print([True, False, True])
# Who came to our shop ?print("1 Customer")
# Who is that ?print(["Khairi Bin Abu Bakar", 720102121234, 1255.25, "Radio", 1, 623.45])
# In other programming languages we cannot put data of different types
# into a single box. They are called "homogeneous" list
# However in python we can put data of different types# into a single box. So it is called "heterogeneous" list
# In python the built in function print has many features
# the print function takes any number of arguments
# where are you going ?print("Shopping", "Cinema") 
# now you are passing 2 arguments to the print function
# the arguments are seperated by comma
# However the output does not have comma
# What are you going to buy ?print("Television", ["apple", "orange", "mango"]) 
# again we are passing 2 arguments
# the first one is string and second one is list of strings
# the output does not have comman but to differentiate the items inside the list
# the comma still appearsprint("Television", 10, 1455.55, True) 
# we are passing 4 arguments to print function
# Questionsprint("Television", 10, "RM", 1455.55, True) 
# you will have a space 
# "RM" is string literal 1455.55 is float literalprint("Television", 10, "RM1455.55", True) 
# you won't have space# RM1455.55 is string literal
# When it prints string we do not have double quote printed
# When it prints the items inside the list which is string then it prints single quoteprint("Television", ["apple", "orange"])
# The string literal can be enclosed with double quote "" or single quote ''
# print function convert the entire list into a string and print it
# "['apple', 'orange']"
# packing / unpacking / iterating
# putting the balls inside the box = packing
# throwing the balls from the box = unpacking
# pulling out the balls one by one from the box = iterating
# I want to know the total amount to be paid when i buy
# 10 TVs and each cost me 1455.55print("Price of", 10, "TVs", "RM", 10 * 1455.55)

# Variables
# Variables are placeholders where we can keep the values

product = "Television"
# product is the placeholder / variable
# The string literal/string value "Television" is assigned to the variable product
# Over here "=" is an assignment operator
# Note: product is also alphabet, Television is also alphabet
# How python knows one is variable and another one is literal ??
# The double quote/single quote is the one that differentiate 
# variable from literal

quantity = 10
# quantity is a placeholder
# The integer literal 10 is assigned to the variable quantity

price = 1455.55
# price is a placeholder
# The float literal 1455.55 is assigned to the variable price

print(product, quantity, price, quantity * price) # we are passing 4 arguments
# every argument is not enclosed with double quote or single quote
# print function treat them as variables and find the values which are inside
# to those variable and prints them

# x is variable and 10 is literal
# x is holding the address location of 10
x = 10
print(x) # the value gets printed
# you can use another built in function id to see what you have in x
# to see the address where the object 10 is
print(id(x)) 
# we are calling id function by passing x variable as argument
# the id function will return the address
# which is again passed as an argument to the print function
# you can use another built in function hex to see the address in hexadecimal
print(hex(id(x)))

x = 11
print(x)
print(id(x))
print(hex(id(x)))

y = 11 # memory scanning will point to the same memory location
print(y)
print(id(y))
print(hex(id(y)))

x = "Television"
print(x)
print(id(x))
print(hex(id(x)))