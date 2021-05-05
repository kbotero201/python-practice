# Python Function Code Challenges

# First Three Multiples
# Write a function named first_three_multiples() that has one parameter named num.
# This function should print the first three multiples of num. Then, it should return the third multiple.
# For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.

def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3

first_three_multiples(10)
first_three_multiples(0)

# Tip 
# Create a function called tip() that has two parameters named total and percentage.
# This function should return the amount you should tip given a total and the percentage you want to tip.

def tip(total, percentage):
  tip_amount = (total * percentage) / 100
  return tip_amount

print(tip(10, 25))
print(tip(0, 100))

# Dog Years 
# Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named dog_years() that has two parameters named name and age.
# The function should compute the age in dog years and return the following string:
# "{name}, you are {age} years old in dog years"

def dog_years(name, age):
  return name + ", you are " + str(age * 7) + " years old in dog years"

print(dog_years("Lola", 16))
print(dog_years("Baby", 0))

# All Operations 
# Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value.
# First, print the sum of a and b.
# Second, print c minus d.
# Third, print the first number printed, multiplied by the second number printed.
# Finally, return the third number printed modulo a.

def lots_of_math(a, b, c, d):
  first = a + b
  second = c - d
  third = first * second
  fourth = third % a
  print(first)
  print(second)
  print(third)
  return fourth

print(lots_of_math(1, 2, 3, 4))
print(lots_of_math(1, 1, 1, 1))
