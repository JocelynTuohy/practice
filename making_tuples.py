# Dictionary In, Tuples Out Assignment

# Write a function that takes in a dictionary and returns a list of tuples where
# the first tuple is the key and the second is the value.

# input
MY_DICT = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}

# function
def dict_in_tuples_out(dictionary):
    tuple_list = []
    for key, data in dictionary.iteritems():
        tuple_list.append((key, data))
    print tuple_list

dict_in_tuples_out(MY_DICT)