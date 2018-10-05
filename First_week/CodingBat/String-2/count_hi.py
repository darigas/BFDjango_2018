def count_hi(str):
  count = 0
  for item in range(len(str) - 1):
    if str[item] == "h"and str[item + 1] == "i":
      count += 1
  return count
