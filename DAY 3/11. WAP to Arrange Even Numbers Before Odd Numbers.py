n = int(input("Enter the size of the list: "))

arr = list(map(int, input("Enter the numbers: ").split()))

even = []
odd = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

result = even + odd

print(*result)