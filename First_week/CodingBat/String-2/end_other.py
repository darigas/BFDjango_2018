def end_other(a, b):
  newA = a.lower()
  newB = b.lower()
  if newA.endswith(newB) or newB.endswith(newA):
    return True
  return False