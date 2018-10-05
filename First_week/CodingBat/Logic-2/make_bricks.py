def make_bricks(small, big, goal):
  if goal / 5 <= big:
    goal -= (goal / 5) * 5
  else:
    goal -= big * 5
  
  if goal <= small:
    return True
  return False
