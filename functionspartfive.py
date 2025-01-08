#scope of variables

message = "welcome to python" #global variable

#bad use of global variable
def sayHello():
    print(message)
sayHello()

def sayHello2(a):
    print(a)
sayHello2("message") #This will use the local variable

def outer():
    message = "Message for outer function"
    def inner():
        print(message)
    inner()
outer()


#modify global variable

x = 10
print("x global is ",x)

def modify():
    global x #global variable will be modified
    x = 20
    print("x inside is ",x)

modify()
print("x global is ",x)

