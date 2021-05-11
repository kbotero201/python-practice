# Python String Code Challenges 

# Check Name 
# Write a function called check_for_name that takes two strings as parameters named sentence and name. The function should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of uppercase and lowercase letters. 
# The function should return False otherwise.
# For example, the following three calls should all return True:
# check_for_name("My name is Jamie", "Jamie")
# check_for_name("My name is jamie", "Jamie")
# check_for_name("My name is JAMIE", "Jamie")

def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

print(check_for_name("My name is Jamie", "Jamie"))
print(check_for_name("My name is jamie", "Jamie"))
print(check_for_name("My name is Samantha", "Jamie"))


# Every Other Letter 
# Create a function named every_other_letter that takes a string named word as a parameter. The function should return a string containing every other letter in word.

def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

print(every_other_letter("Codecademy"))
print(every_other_letter("Hello world!"))
print(every_other_letter(""))


# Reverse 
# Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.

def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse

print(reverse_string("Codecademy"))
print(reverse_string("Hello world!"))
print(reverse_string(""))


# Make Spoonerism
# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. Finding the first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each word. Return the two new words as a single string separated by a space.

def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

print(make_spoonerism("Codecademy", "Learn"))
print(make_spoonerism("Hello", "world!"))
print(make_spoonerism("a", "b"))

# Add Exclamation
# Create a function named add_exclamation that has one parameter named word. 
# This function should add exclamation points to the end of word until word is 20 characters long. 
# If word is already at least 20 characters long, just return word.

def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word

print(add_exclamation("Codecademy"))
print(add_exclamation("Codecademy is the best place to learn"))

