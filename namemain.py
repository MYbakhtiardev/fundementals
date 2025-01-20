class Student:
    def __init__(self, fname):
        self.fname = fname
    
    def __str__(self):
        return f"{self.fname}"


if __name__ == "__main__":
    myStudent = Student("John")
    print(myStudent)