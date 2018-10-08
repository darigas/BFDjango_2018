 def count_code(str):
  count = 0
  for item in range(len(str) - 3):
    if str[item] == "c" and str[item + 1] == "o" and str[item + 3] == "e":
      count += 1
  return count
