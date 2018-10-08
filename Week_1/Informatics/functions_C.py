def xor(x, y):
	if (x == y):
		return 0
	else:
		return 1

given = input().split()

print(xor(given[0], given[1]))