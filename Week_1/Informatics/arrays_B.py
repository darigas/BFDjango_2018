N = int(input())
numbers = input().split()

for item in range(0, N):
	if (int(numbers[item]) % 2 == 0):
		print(numbers[item])