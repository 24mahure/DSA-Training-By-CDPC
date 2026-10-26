arr = [0, 1, 0, 3, 12]

for i in arr:
    if i == 0:
        arr.remove(i)
        arr.append(0)

print(arr)