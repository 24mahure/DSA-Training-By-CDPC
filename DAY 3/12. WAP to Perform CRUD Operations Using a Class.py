import sys

class CRUD:
    def __init__(self):
        print("School Management System")

        self.studentsid = []
        self.studentsname = []
        self.studentrollno = []
        self.studentcity = []

    def add_student(self):
        self.studentsid.append(input("Enter student ID: "))
        self.studentsname.append(input("Enter student name: "))
        self.studentrollno.append(input("Enter student roll number: "))
        self.studentcity.append(input("Enter student city: "))

    def show_students(self):
        if not self.studentsid:
            print("No student records found.")
            return

        print("Student Details")

        print("Student ID | Name | Roll Number | City")

        for i in range(len(self.studentsid)):
            print(
                self.studentsid[i],
                self.studentsname[i],
                self.studentrollno[i],
                self.studentcity[i]
            )

    def update_student(self):
        id = input("Enter student ID to update: ")

        if id in self.studentsid:
            index = self.studentsid.index(id)

            self.studentsname[index] = input("Enter new student name: ")
            self.studentrollno[index] = input("Enter new student roll number: ")
            self.studentcity[index] = input("Enter new student city: ")

            print("Student updated successfully.")

        else:
            print("Student ID not found.")

    def delete_student(self):
        id = input("Enter student ID to delete: ")

        if id in self.studentsid:
            index = self.studentsid.index(id)

            del self.studentsid[index]
            del self.studentsname[index]
            del self.studentrollno[index]
            del self.studentcity[index]

            print("Student deleted successfully.")

        else:
            print("Student ID not found.")

    def start(self):
        while True:
            print("\n1. Add Student")
            print("2. Show Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()

            elif choice == '2':
                self.show_students()

            elif choice == '3':
                self.update_student()

            elif choice == '4':
                self.delete_student()

            elif choice == '5':
                sys.exit()

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    obj = CRUD()
    obj.start()