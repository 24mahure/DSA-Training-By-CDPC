A = []
B = []

n1 = int(input("Enter the size of first array: "))

for i in range(n1):
    A.append(input())

n2 = int(input("Enter the size of second array: "))

for i in range(n2):
    B.append(input())

if len(A) == len(B):
    print("Arrays are compatible")
else:
    print("Arrays are not compatible")