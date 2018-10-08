def string_splosion(str):
  result = ""
  for item in range(len(str)):
    result += str[:item + 1]
  return result
