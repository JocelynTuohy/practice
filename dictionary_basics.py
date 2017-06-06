# Making and Reading from Dictionaries Assignment
# Create a dictionary containing some information about yourself. The keys
# should include name, age, country of birth, and favorite language. Print out
# the result as in the example.

SELFDICT = {
    'name' : 'Jocelyn',
    'age' : '32',
    'country of birth' : 'the United States',
    'favorite langugage' : 'Mandarin Chinese'
}

def readOut(dictionary):
    for key, data in SELFDICT.iteritems():
        print 'My ' + key + ' is ' + data

readOut(SELFDICT)