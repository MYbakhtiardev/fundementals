#Syntax error
#Logical error
#Runtime error

#Syntax error
# print("Hello")
# print("Hello")
# print("Hello")

#Logical error
x = 10
y = 3
# print(x + y)

#Runtime error
x = 10
y = 0
# print(x / y)

x = input("Enter a number: ")
try:
    x = int(x)
    print(x)
except():
    print("Error. Please enter a number.")
else:
    print(x)
print("Hello")


def divide_numbers(a, b):
    try:
        result = a / b  # Attempt to divide
    except ZeroDivisionError:
        # This block will run if there's a division by zero
        print("Error: Cannot divide by zero.")
    else:
        # This block will run only if no error occurs
        print(f"The result is {result}")

# Test cases
divide_numbers(10, 2)  # Normal division
divide_numbers(10, 0)  # Division by zero

# Syntax Error

"""
givenNumber = 4
if givenNumber % 2 == 0:
print("Given Number:", givenNumber)
print("Even Number")
"""

# Logical Error
# Usually in a programming environment this type of errors is a bit difficult to
# identify and fix it
# Usually the end user will highlight this error to us
"""
givenNumber = 5
if givenNumber % 2 == 0:
    print("Given Number:", givenNumber)
print("Even Number")
"""

# Runtime errors
# Usually caused because of Input and Output (I/O)
# So statements that involved with Input and Output must be enclosed 
# with try except block
# The problem is it throws more technical error to the user 
# and the user wont understand the error
# The program abnormally gets terminated
x = input("Please key in a number: ")
try:
    # the code that might throw error in future 
    # can go inside this try block
    x = int(x)
except:
    # the code that is suppose to be executed when the error occurs
    # must go inside here
    print("Input must be a number. Cannot be a string")
else:
    # this try except block can also have else block
    # the code that is suppose to be executed when no error occurs
    # must go inside her
    print(x)
finally:
    # this try except block can also have finally block
    # the code inside the finally block always gets exected
    # regardless of whether an error occur or not
    print("Close the resources")

print("Hello") # since abnormally terminiated this line will never gets executed

isInvalid = True
while isInvalid:
    x = input("Some number: ")
    try:
        x = int(x)
    except:
        print("Input must be integer")
    else:
        isInvalid = False

print(x)
print("Thank you")


# the int function when it tries to convert the input into an integer
# if it cannot convert then it throw us an error using a keyword "raise"
# Since the function throw us the error we are able to capture the error 
# inside the try excect block
def checkBalance(balance):
    """
    if balance < 10:
        # print("Insufficient Balance") # if we just print then no way for us to check
        return False
    else:
        return True
    """
    if balance < 10: raise Exception("Insufficient Balance")

"""
if checkBalance(balance):
    balance = balance - withdraw
else:
    print("Insufficient Balance")
"""
balance = 5
withdraw = 3
try:
    checkBalance(balance)
except Exception as e:
    print(e)
else:
    balance = balance - withdraw
