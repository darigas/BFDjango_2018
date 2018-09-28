def cat_dog(str):
  countCat = 0
  countDog = 0
  for item in range(len(str) - 2):
    if str[item] == "c" and str[item + 1] == "a" and str[item + 2] == "t":
      countCat += 1
    if str[item] == "d" and str[item + 1] == "o" and str[item + 2] == "g":
      countDog += 1
  if countCat == countDog:
    return True
  return False
