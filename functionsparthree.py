def sayHello():
    print("Hello")

print(type(sayHello))
sayHello()

x = 10
print(type(x))

Welcome = sayHello
Welcome() #calling the function as a variable or object #Hello

Welcome = sayHello()
print(Welcome) #None as the function doesn't return anything

def greeting(func):
    func()

def sayGoodMorning():
    print("Good Morning")

def sayGoodAfternoon():
    print("Good Afternoon")

greeting(sayGoodMorning)
greeting(sayGoodAfternoon)


#Functional programming
def mouseClick(func):
    func()

def iconClick():
    print("Icon Clicked")

def clickEvent():
    mouseClick(iconClick)

clickEvent()


celcius_value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def convertToFahrenheit(celcius_value):
    return celcius_value * (9/5) + 32
Fahrenheit_values = list(map(convertToFahrenheit, celcius_value))
print(Fahrenheit_values)


given_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def isEven(given_number):
    return given_number % 2 == 0
even_numbers = list(filter(isEven, given_number))
print(even_numbers)