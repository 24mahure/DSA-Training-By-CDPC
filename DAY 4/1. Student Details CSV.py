import csv
f = open("students.csv", "a",newline="")
a=csv.writer(f)
a.writerow(["studentID","rollno","name",'mobileno','p1','p2','p3','total','percentage','email']) # devlop logic to write this line once only
studentID = input("Enter student ID: ")
rollno = input("Enter roll number: ")
name = input("Enter student name: ")
mobileno = input("Enter mobile number: ")
p1 = input("Enter marks for subject 1: ")
p2 = input("Enter marks for subject 2: ")
p3 = input("Enter marks for subject 3: ")
email = input("Enter email: ")
total = int(p1) + int(p2) + int(p3)
percentage = (total / 300) * 100
if int(p1) >= 40 and int(p2) >= 40 and int(p3) >= 40:
    result = "pass"
else:
    result = "fail"
a.writerow([studentID, rollno, name, mobileno, p1, p2, p3, total, percentage, email])
print("Data written successfully to students.csv")