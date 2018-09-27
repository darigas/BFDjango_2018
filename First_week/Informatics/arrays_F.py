N = int(input())
numbers = input().split()
check = 0

for item in range(1, N - 1):
	if (int(numbers[item]) > int(numbers[item - 1]) and int(numbers[item]) > int(numbers[item + 1])):
		check += 1

print(check)