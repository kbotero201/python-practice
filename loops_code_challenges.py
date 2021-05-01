# Python Loops Code Challenges

# Larger Sum 
# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))


# Over 9000
# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.
# The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.
# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

print(over_nine_thousand([8000, 900, 120, 5000]))


# Max Num 
# Create a function named max_num() that takes a list of numbers named nums as a parameter.
# The function should return the largest number in nums
# Without using max()

def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

print(max_num([50, -10, 0, 75, 20]))


# Same Values 
# Write a function named same_values() that takes two lists of numbers of equal size as parameters.
# The function should return a list of the indices where the values were equal in lst1 and lst2.
# For example, the following code should return [0, 2, 3]
# same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])



# Reversed List 
# Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.
# The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.
