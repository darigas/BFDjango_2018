def count_evens(nums):
  count = 0
  for item in range(len(nums)):
    if nums[item] % 2 == 0:
      count += 1
  return count