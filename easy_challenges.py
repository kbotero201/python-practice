# In Range CC
# The function should return True if num is greater than or equal to lower and less than or equal to upper.
# Otherwise, return False.

def in_range(num, lower, upper):
    if num >= lower and num <= upper: 
        return True  
    return False 


# Same Name CC
# Create a function named same_name() that has two parameters named your_name and my_name.
# If our names are identical, return True. Otherwise, return False.

def same_name(your_name, my_name):
  if your_name == my_name: 
    return True 
  return False


# Always False CC 
# Create a function named always_false() that has one parameter named num.
# Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num.

def always_false(num):
  if num > 0 and num < 0:
    return True
  else:
    return False
