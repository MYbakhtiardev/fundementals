#Inner func
def outer(message = "Welcome to Python"):
    print("Outer function")
    
    #inner function can only be called inside the outer function
    def inner():
        x = print("Inner function", message)
        return x

    # inner()
    if message != None :
        return inner

outer()

def arithmetic(operation):
    def addition(a, b):
        return a + b
    def subtraction(a, b):
        return a - b
    def multiplication(a, b):
        return a * b
    def division(a, b):
        return a / b
    def modulus(a, b):
        return a % b
    def exponent(a, b):
        return a ** b
    def floor_division(a, b):
        return a // b

    if operation == "+":
        return addition
    elif operation == "-":
        return subtraction
    elif operation == "*":
        return multiplication
    elif operation == "/":
        return division
    elif operation == "%":
        return modulus
    elif operation == "**":
        return exponent
    elif operation == "//":
        return floor_division

print("another example", arithmetic("+")(10, 5))