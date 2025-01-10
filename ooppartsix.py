class Student:

    #global variable    
    counter = 0

    def __init__(self):
        # properties always has self
        self.fname = ""
        self.lname = ""
        self.feeamount = 0

        # this is class variable which is shared by all objects. 
        # every time an object is created it will be incremented
        Student.counter += 1
    
    def calculateFee(self, amount):
        #variables w/o self are local
        result = amount * 1.06
        self.feeamount = result


class Utility:

    def __init__(self): #no property
        pass

    def calculateSI(principle, period, rate):
        result = principle * period * rate / 100
        return result


peter = Student()
#object.var is instance variable/property
peter.fname = "Peter"
peter.lname = "Parker"
peter.feeamount = 7432.50

print(peter.fname)
print(peter.lname)
print(peter.feeamount)

student01 = Student()
student02 = Student()
student03 = Student()
print(Student.counter) #4

print(Utility.calculateSI(1000, 2, 5))