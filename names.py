# Names Assignment
# Practice unpacking lists and dictionaries.

# Part I
STUDENTS = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def print_names_from_list(name_list):
    for each in range(0, len(name_list)):
        print name_list[each]['first_name'], name_list[each]['last_name']

print_names_from_list(STUDENTS)

print ''

# Part II
USERS = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

def print_students_and_instructors(matrix):
    for key in matrix:
        print key
        for each in range(0, len(matrix[key])):
            first_name = matrix[key][each]['first_name'].upper()
            last_name = matrix[key][each]['last_name'].upper()
            print ('1 - ' + first_name + ' ' + last_name + ' - ' +
                   str(len(first_name + last_name)))

print_students_and_instructors(USERS)