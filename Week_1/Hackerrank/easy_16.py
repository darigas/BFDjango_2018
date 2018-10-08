from collections import Counter

numberShoes = int(input())
shoes = Counter(map(int, input().split()))
numCustomers = int(input())

income = 0

for item in range(numCustomers):
	size, price = map(int, input().split())
	if shoes[size]:
		income += price
		shoes[size] -= 1

print(income)
