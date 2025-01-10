class Student:

    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.icnumber = ""
    
    def __str__(self):
        return f"""
        First Name: {self.firstname}
        Last Name: {self.lastname}
        IC Number: {self.icnumber}
        """

class Alumni(Student):
    
    def __init__(self):
        super().__init__()
        # super()
        # self.alumninumber = ""
    
    def __str__(self):
        result = super().__str__()
        result += f"""Alumni Number: {self.alumninumber}
        """
        return result

john = Alumni()
john.firstname = "John"
john.lastname = "Doe"
john.icnumber = 123456789
john.alumninumber = 123456

print(john)