s = input()
alpha = False
alnum = False
digit = False
low = False
up = False
for item in s:
	if item.isalnum():
		alnum = True
	if item.isalpha():
		alpha = True
	if item.isdigit():
		digit = True
	if item.islower():
		low = True
	if item.isupper():
		up = True

print(alnum)
print(alpha)
print(digit)
print(low)
print(up)