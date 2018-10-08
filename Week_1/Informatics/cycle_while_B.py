N = int(input())
number = 2
min = 1

while (number <= N):
	if (N % number == 0):
		min = number
		print(number)
		break
	number += 1