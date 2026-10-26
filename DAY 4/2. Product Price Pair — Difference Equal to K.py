n = int(input("Enter the number of product types: "))
k = int(input("Enter the value of K: "))
prices = list(map(int, input("Enter the prices of the products: ").split()))

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if abs(prices[i] - prices[j]) == k:
            count += 1

print("The total number of lucky customers who will get the gift hampers is:", count)