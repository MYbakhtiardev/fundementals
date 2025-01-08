# arithmetics in python
# +, -, *, /, %, **, //

x = 10
y = 3
print(x + y) #addition
print(x - y) #subtraction
print(x * y) #multiplication
print(x / y) #division
print(x % y) #modulus (remainder)
print(x ** y) #exponent (raise to the power)
print(x // y) #floor division (quotient) result rounded down to the nearest integer

#unary operators
x = 10
print(+x) #positive
print(-x) #negative

#for string + and * is concatenation
x = "Hello"
y = "World"
print(x + y)

x = "Hello"
y = 3
print(x * y)

#assignment operators
x = 10
y = 3
x += y
print(x) #x = x + y = 13

x = 10
y = 3
x -= y
print(x) #x = x - y = 7

x = 10
y = 3
x *= y
print(x) #x = x * y = 30

x = 10
y = 3
x /= y
print(x) #x = x / y = 3.33333

x = 10
y = 3
x %= y
print(x) #x = x % y = 1

x = 10
y = 3
x **= y
print(x) #x = x ** y = 1000

x = 10
y = 3
x //= y
print(x) #x = x // y = 3

#comparison operators
x = 10
y = 3
print(x == y) #equal to
print(x != y) #not equal to
print(x > y) #greater than
print(x < y) #less than
print(x >= y) #greater than or equal to
print(x <= y) #less than or equal to

#logical operators
x = True
y = False
print(x and y) #and (&&)
print(x or y) #or (||)
print(not x) #not (!)
print(x ^ y) #xor

#identity operators
x = 10
y = 10
print(x is y) #is (==)
print(x is not y) #is not (!=)

#membership operators
x = [1, 2, 3]
y = 2
print(y in x) #in
print(y not in x) #not in

#bitwise operators
x = 10
y = 3
print(bin(x))
print(bin(y))
print(x & y) #and (&)
print("binary of x & y",bin(x & y))
print(x | y) #or (|)
print("binary of x | y", bin(x | y))
print(x ^ y) #xor (^)
print("binary of x ^ y", bin(x ^ y))
print(~x) #not (~)
print(bin(~x))
print(x << y) #left shift (<<)
print("binary of x << y", bin(x << y))
print(x >> y) #right shift (>>)
print("binary of x >> y", bin(x >> y))