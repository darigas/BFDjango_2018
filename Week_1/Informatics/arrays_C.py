N = int(input())
numbers = input().split()
cnt = 0

for item in range(0, N):
	if (int(numbers[item]) > 0):
		cnt += 1
print(cnt)
