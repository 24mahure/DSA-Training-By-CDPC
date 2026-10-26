roll_num = [3, 5, 7, 1, 11, 4, 5, 2]

for x in roll_num:
    if x % 2 == 0:
        print("First even number:", x)
        break
else:
    print("even not found")