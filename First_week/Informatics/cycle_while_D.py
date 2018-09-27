N = int(input())

number = 1
i = 0

while(N >= 1):
	i = i + N % 2
	N = N / 2

if (i == 1):
	print("YES")
else:
	print("NO")