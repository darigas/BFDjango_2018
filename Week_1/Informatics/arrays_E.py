N = int(input())
numbers = input().split()
truecnt = 0
truecnt = 0

for item in range(1, N):
	if (int(numbers[item]) * int(numbers[item - 1]) > 0):
		truecnt += 1

if (truecnt >= 1):
	print ("YES")
else:
	print("NO)