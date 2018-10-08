given = input().split()

def double_power(a, n):
	result = 1
	for item in range(n):
		result = result * a
	print(result)

double_power(float(given[0]), int(given[1]))