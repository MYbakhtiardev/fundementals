class classA:
    def __init__(self):
        self.x = 10
        print("class A")

class classB(classA):
    def __init__(self):
        super().__init__()
        print("Class B extend class A")

class classC(classA):
    def __init__(self):
        super().__init__()
        print("Class C extend class A")

class classD(classB):
    def __init__(self):
        super().__init__()
        print("Class D extend class B")

class classE(classC):
    def __init__(self):
        super().__init__()
        print("Class E extend class C")


myObject = classE()
print(myObject.x)

class Left():
    def __init__(self):
        self.x = 10
        self.y = 987

    def __str__(self):
        return f"""
        Left x: {self.x}, 
        Left y: {self.y},"""

class Right():
    def __init__(self):
        self.x = 20
        self.y = 25
        self.z = 699

    def __str__(self):
        return f"""
        Right x: {self.x}, 
        Right y: {self.y}, 
        RIght z: {self.z},"""

class MyClass(Left, Right):
    def __init__(self):
        super().__init__() # This calls Left.__init__() (since Left comes first in MRO)
        # Left.__init__(self)
        Right.__init__(self) # Manually call Right.__init__() because super() skips Right
        self.x = 30
        # print(self.x)
        # print(self.y)
    
    def __str__(self):
        result = super().__str__()
        result += Right.__str__(self)
        result += f"""
        My Class x: {self.x}
        """
        return result
        

myClass = MyClass()
print(myClass)
print("mx",myClass.x)
print("my",myClass.y)
print("mz",myClass.z)
print("\tr\u0332e\u0332s\u0332",myClass)

# print(MyClass.__mro__)

