class Student:
    def __init__(self):
        self.name = input("Enter name: ")
        self.mobileno = int(input("Enter mobile number: "))
        self.emailid = input("Enter email ID: ")
        self.rollno = int(input("Enter roll number: "))
        self.branch = input("Enter branch: ")

obj = Student()

print(obj.__dict__)