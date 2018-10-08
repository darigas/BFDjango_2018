def double_char(str):
  result = ""
  for item in range(len(str)):
    result += str[item] + str[item]
  return result
