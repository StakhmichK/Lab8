from decimal import Decimal

price = Decimal(input("Enter the price: "))

total = price * 100

hryvnias = int(total // 100)
kopecks = int(total % 100)

print(hryvnias, kopecks)