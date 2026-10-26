import sys
class CRUD:
    def __init__(self):
        print("Student Management System initialized.")
        self.studentID=[]
        self.studentName=[]
        self.studentRollNo=[]
        self.studentCity=[]

    def addStudent(self):
        id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        rollNo = input("Enter Student Roll Number: ")
        city = input("Enter Student City: ")

        self.studentID.append(id)
        self.studentName.append(name)
        self.studentRollNo.append(rollNo)
        self.studentCity.append(city)

    def showStudents(self):
        print("Student Details are: \n")
        print("Student ID\tStudent Name\tStudent Roll Number\tStudent City")
        for x in range(80):
            print("-", end="")
        print()
        for i in range(len(self.studentID)):
            print(f"{self.studentID[i]}\t\t{self.studentName[i]}\t\t{self.studentRollNo[i]}\t\t{self.studentCity[i]}")

            for x in range(80):print("-", end="")
            print()

    def updateStudent(self):
        id = input("Enter Student Id to update:")
        if id in self.studentID:
            print("1. Student ID:",id)
            print("2. Student Name:",self.studentName[self.studentID.index(id)])
            print("3. Student Roll Number:",self.studentRollNo[self.studentID.index(id)])
            print("4. Student City:",self.studentCity[self.studentID.index(id)])
            print("5. Cancel")
            print("Enter choice to update:")
            choice = input()
            if choice == "1":
                new_id = input("Enter new Student ID: ")
                self.studentID[self.studentID.index(id)] = new_id
            elif choice == "2":
                new_name = input("Enter new Student Name: ")
                self.studentName[self.studentID.index(id)] = new_name
            elif choice == "3":
                new_rollNo = input("Enter new Student Roll Number: ")
                self.studentRollNo[self.studentID.index(id)] = new_rollNo
            elif choice == "4":
                new_city = input("Enter new Student City: ")
                self.studentCity[self.studentID.index(id)] = new_city
            elif choice == "5":
                print("Dont want to update anything.")
                pass
            else:
                print("Invalid choice.")
        else:
            print("Student not found.")

    def deleteStudent(self):
        id = input("Enter Student  ID to delete:")
        if id in self.studentID:
            index = self.studentID.index(id)
            del self.studentCity[index]
            del self.studentRollNo[index]
            del self.studentName[index]
            del self.studentID[index]

    def menu(self):
        while True:
            print("1. Add Student")
            print("2. Show Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.addStudent()
            elif choice == "2":
                self.showStudents()
            elif choice == "3":
                self.updateStudent()
            elif choice == "4":
                self.deleteStudent()
            elif choice == "5":
                sys.exit()
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    crud = CRUD()
    crud.menu()