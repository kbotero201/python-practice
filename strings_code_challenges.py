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



# Reverse 
# Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.



# Make Spoonerism
# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. Finding the first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each word. Return the two new words as a single string separated by a space.



# Add Exclamation
# Create a function named add_exclamation that has one parameter named word. 
# This function should add exclamation points to the end of word until word is 20 characters long. 
# If word is already at least 20 characters long, just return word.

