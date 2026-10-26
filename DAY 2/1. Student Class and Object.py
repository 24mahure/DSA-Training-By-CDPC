class Student:
    rollno = 101

    def __init__(self):
        print("Constructor is called")

    def msg(self):
        print("Hello")

obj = Student()

print(obj)
obj.msg()

obj1 = Student()

print(obj.rollno)