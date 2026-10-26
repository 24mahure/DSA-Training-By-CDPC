M1 = int(input("Enter the marks of M1: "))
M2 = int(input("Enter the marks of M2: "))
M3 = int(input("Enter the marks of M3: "))

total = M1 + M2 + M3
percentage = total / 3.0

print("Total marks:", total)
print("Percentage:", percentage)

if M1 >= 40 and M2 >= 40 and M3 >= 40:
    print("Pass")

    if percentage > 65:
        project = input("Do you have a project? (yes/no): ")

        if project.lower() == 'yes':
            print("Eligible for placement drive")
        else:
            print("Not eligible for placement drive")
    else:
        print("Not eligible for placement drive due to low percentage")

else:
    print("Fail")