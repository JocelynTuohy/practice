# Type List Assignment
## Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it
## onto a new string. If it is a number, add it to a running sum. At the end of your program print the string,
## the number and an analysis of what the array contains. If it contains only one type, print that type, otherwise, print 'mixed'.

# input will always be a list
inputList = [2-3j,"talk",3]

# declare variables
stringage = 'String:'
summage = 0
hasString = False
hasInt = False
hasFloat = False
hasOther = False

# loop through the list
for member in inputList:
  if type(member) == str:
    stringage = stringage + ' ' + member
    hasString = True
  elif type(member) == int:
    summage += member
    hasInt = True
  elif type(member) == float:
    summage += member
    hasFloat = True
  else:
    hasOther = True
if (hasString and hasInt) or (hasString and hasFloat) or (hasString and hasOther) or (hasFloat and hasInt) or (hasFloat and hasOther) or (hasInt and hasOther):
  print 'The array you entered is of mixed type'
elif hasOther:
  print 'You entered some weirdass array'
elif hasString:
  print 'The array you entered is of string type'
elif hasInt:
  print 'The array you entered is of integer type'
elif hasFloat:
  print 'The array you entered is of float type'

print stringage
print 'Sum: ' + str(summage)