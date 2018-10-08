def fix_teen(n):
  if n < 13 or n > 19 or n == 15 or n == 16:
    return n
  return 0

def no_teen_sum(a, b, c):
  new_a = fix_teen(a)
  new_b = fix_teen(b)
  new_c = fix_teen(c)
  return new_a + new_b + new_c
  
    