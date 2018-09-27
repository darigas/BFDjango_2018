N = int(input())
numbers = input().split()
cnt = 0

for item in range(1, N):
	if (int(numbers[item - 1]) < int(numbers[item])):
		cnt += 1

print(cnt)