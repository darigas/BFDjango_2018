from math import sqrt
a = int(input())
b = int(input())
for number in range(a, b + 1):
	t = int(sqrt(number))
	if (t * t == number):
		print(number)