import math

N = int(input())
number = 1
x = int(number * number)

while (x <= N):
	print(x)
	number += 1
	x = number * number