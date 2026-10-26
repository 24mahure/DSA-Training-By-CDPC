pizza = 100
burger = 50
coldrink = 20

val1 = int(input("Enter the number of pizza: "))
val2 = int(input("Enter the number of burger: "))
val3 = int(input("Enter the number of coldrink: "))

pizza_total = pizza * val1
burger_total = burger * val2
coldrink_total = coldrink * val3

print("-----------------------------------------------")
print("Bill Details")
print("Pizza:", pizza_total)
print("Burger:", burger_total)
print("Coldrink:", coldrink_total)

print("Total:", pizza_total + burger_total + coldrink_total)
print("-----------------------------------------------")