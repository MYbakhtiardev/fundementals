class Passport:
    def __init__(self):
        self.passport_number = ""
        self.country = ""
        self.visa_number = ""
        self.visa_expiry_date = ""

    def __str__(self):
        result = f"""
        Passport Number: {self.passport_number}
        Country: {self.country}
        Visa Number: {self.visa_number}
        Visa Expiry Date: {self.visa_expiry_date}
        """
        return result


class Student:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.phone_no = ""
        self.email = ""
        self.ic_number = ""
        self.passport = None

    def __str__(self):
        result = f"""
        Name: {self.name}
        Age: {self.age}
        Phone Number: {self.phone_no}
        Email: {self.email}
        IC Number: {self.ic_number}
        Passport: {self.passport}
        """
        return result

john = Student()
john.name = "John"
john.age = 20
john.phone_no = "1234567890"
john.email = "John@hmail.com"
john.ic_number = None
johnpassport = Passport()
johnpassport.passport_number = "A1234567"
johnpassport.country = "Singapore"
johnpassport.visa_number = "V1234567"
johnpassport.visa_expiry_date = "2022-01-01"
john.passport = johnpassport

print(john)


##class list have __str__ method that returns a string representation of the list