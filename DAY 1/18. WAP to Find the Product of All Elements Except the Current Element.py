arr = [1, 2, 3, 4]

for i in arr:
    product = 1

    for j in arr:
        if i != j:
            product *= j

    print(product, end=' ')