# Find Characters Assignment
# Write a program that takes a list of strings and a string containing a single character, and
# prints a new list of all the strings containing that character.

# Test Input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'

new_list = []
# loop through list
for word in word_list:
  # loop through letters
  for letter in word:
    if letter == char:
      new_list.append(word)
      break
print new_list