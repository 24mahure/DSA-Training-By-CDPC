class Student:
    def __init__(self, name, mobile_no, email_id):
        self.name = name
        self.mobileno = mobile_no
        self.emailid = email_id

    def display_info(self):
        print("Name:", self.name)
        print("Mobile No:", self.mobileno)
        print("Email ID:", self.emailid)

student = Student(
    input("Enter name: "),
    input("Enter mobile number: "),
    input("Enter email ID: ")
)

student.display_info()