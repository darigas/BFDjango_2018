N = int(input())
k = 0
cnt = 0
for number in range(0, N):
	k = int(input())
	if (k == 0):
		cnt += 1
print(cnt)