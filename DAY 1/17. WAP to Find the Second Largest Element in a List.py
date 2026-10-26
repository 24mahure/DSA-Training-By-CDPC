arr = [7, 3, 9, 2, 8]

second_largest = arr[0]
largest = arr[0]

for i in arr:
    if i > largest:
        second_largest = largest
        largest = i

    elif i > second_largest and i != largest:
        second_largest = i

print("Second largest:", second_largest)