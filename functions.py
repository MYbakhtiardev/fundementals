#function is to perform a task
#function is a block of code that is executed when it is called
#function is defined by def keyword

def my_function():
    print("Hello from a function")

my_function()

def even_or_odd(given_number):
    if given_number % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_or_odd(9)

def calculateInterest(principal, rate, time):
    interest = principal * rate * time / 100
    print("Interest is", interest)

calculateInterest(10000, 10, 5)

def simpleCalculateInterest(principal, rate, time):
    interest = principal * rate * time / 100
    return interest

result = simpleCalculateInterest(10000, 10, 5)
print("Interest is", result)

def calculator(operation, num1, num2):
    switch = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2
    }
    return switch.get(operation, "Invalid operation")

result = calculator("+", 10, 5)
print("Result is", result)

def calculator(operation, num1, num2, num3 = 5): #default value
    switch = {
        "+": num1 + num2 + num3,
        "-": num1 - num2 - num3,
        "*": num1 * num2 * num3,
        "/": num1 / num2 / num3
    }
    return switch.get(operation, "Invalid operation")

print("Result is", calculator("+", 10, 5))
print("Result is", calculator("+", 10, 5, 10))

#for argument with no position
def calculator(operation, num1, num2, num3 = 5):
    switch = {
        "+": num1 + num2 + num3,
        "-": num1 - num2 - num3,
        "*": num1 * num2 * num3,
        "/": num1 / num2 / num3
    }
    return switch.get(operation, "Invalid operation")

print("Result is unp", calculator(num3=10, operation="+", num1=10, num2=5)) #add parameter name with value

def plot(data, title = "Plot", font_color = "black", font_size = 10, line_color = "red", line_size = 1):
    print("Data: ", data)
    print("Title: ", title)
    print("Font color: ", font_color)
    print("Font size: ", font_size)
    print("Line color: ", line_color)
    print("Line size: ", line_size)

plot([1, 2, 3, 4, 5], "My Data", "blue", 15, "green", 2)