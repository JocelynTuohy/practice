# Making Dictionaries Assignment

# Create a function that takes in two lists and creates a single dictionary
# where the first list contains keys and the second values. Assume the lists
# will be of equal length.

# Hacker Challenge:
# If the lists are of unequal length, the longer list should be used for the
# keys, the shorter for the values.

# input
NAME = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "WHOA",
        'legendary', 'fountain pen', 'fan']
FAVORITE_ANIMAL = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins",
                   "llamas"]

# function
def make_dict(arr1, arr2):
    new_dict = {}
    if len(arr1) >= len(arr2):
        key_list = arr1
        value_list = arr2
    else:
        key_list = arr2
        value_list = arr1
    for item in range(0,len(value_list)):
        new_dict[key_list[item]] = value_list[item]
    if len(key_list) > len(value_list):
        for item2 in range(len(value_list),len(key_list)):
            new_dict[key_list[item2]] = None
    return new_dict

# call function
print make_dict(NAME, FAVORITE_ANIMAL)
