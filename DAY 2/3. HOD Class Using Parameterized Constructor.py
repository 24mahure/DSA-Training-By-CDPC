class Hod:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.empid = rollno

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Empid:", self.empid)

hod = Hod("Arjun", 45, 101)
hod.show()