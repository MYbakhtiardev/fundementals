# Encapsulation
# Capsule: It protects the medicine (in powder form)
# It will get oxidized

# In Class we do have properties and we want to encapsulate them
# Currently it is open for anybody to assign any value
class bankAccount:

    # Now my constructor is take 3 parameters
    # Value for the First parameter will be handle by python
    # If anybody want to create an object of bankAccount
    # they must send the accountNumber and accountName
    def __init__(self, accountNumber, accountName):
        # we can take the parameter variable and 
        # assign it to the property
        self.__accountNumber = accountNumber # property preceeded using __ are private
        self.__accountName = accountName
        self.currentBalance = 0

    # Getter Method
    def getAccountNumber(self):
        return self.__accountNumber
    
    # Setter Method
    def setAccountNumber(self, accountNumber):
        try:
            values = accountNumber.split("-") # accountNumber = "ABCD-EFGH-3456-7890"
            if len(values) == 4: # values = ["ABCD", "EFGH", "3456", "7890"]
                for value in values:
                    if len(value) == 4: # ABCD
                        result = int(value)
                    else:
                        raise Exception("Invalid Account Number")        
            else:
                # raise is another keyword in python that help us to throw errors
                # Exception is another class we created an instance of the 
                # Exception class with value "Invalid Accout Number" and throw the error
                e = Exception("Invalid Account Number")
                raise e
        except:
            raise Exception("Invalid Account Number")
        else:
            self.__accountNumber = accountNumber

    # this is how you create a new property called accountNumber
    accountNumber = property(getAccountNumber, setAccountNumber)

    def __str__(self):
        return f"""Account Number: {self.__accountNumber}
Account Name: {self.__accountName}
CurrentBalance: {self.currentBalance}"""


# can we create a bankaccount without accountnumber
# and accountname
# however in the below case we are able to create a bankaccount
# without accountnumber and accountname
# myBankAccount = bankAccount()

# How do we make those properties are compulsory
myBankAccount01 = bankAccount("1234-5678-9012-3456", "Peter Parker")
myBankAccount01.currentBalance = 1560.25
print(myBankAccount01)

# What happens if i assign the properties with invalid data
myBankAccount02 = bankAccount("5678-9012-3456-7890", "Khairi Bin Abu Bakar")

# myBankAccount02.__accountNumber = "ABCD-EFGH-3456-7890"
# since it is promoted as a private member you cannot update 
# this property value from outside of the class
# This is not what we wanted. We dont want invalid data to be assigned
# However not it becomes like nothing can be assigned
try:
    # myBankAccount02.setAccountNumber("ABCD-EFGH-3456-7890")
    myBankAccount02.accountNumber = "ABCD-EFGH-3456-7890"
except Exception as e:
    print(e)

# how to stop user from assigning invalid data to the property ?
# the answer is encapsulation
myBankAccount02.currentBalance = 7650.15
print(myBankAccount02)


# Encapsulation
# 1) Make the property private
# 2) Create getter and setter methods
# 3) Now use the getter and setter methods to update the properties
# 4) Go to the setter function and do the validation code