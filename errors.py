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
