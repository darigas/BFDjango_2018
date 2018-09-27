import math
a = int(input())
cnt = 0
for x in range(1, int(math.sqrt(a))):
	if a % x == 0: 
		cnt += 1
		
cnt *= 2
if a % math.sqrt(a) == 0: 
	cnt += 1

print(cnt)