# Coin Tosses Assignment (Coding Dojo)
# Write a function that simulates tossing a coin 5,000 times. Your function should print how many
# times the head/tail appears.

import random

def coinToss():
  tailsTot = 0
  headsTot = 0
  print 'Starting the program...'
  for toss in range(1,5001):
    if round(random.random()):
      result = 'head'
      headsTot += 1
    else:
      result = 'tail'
      tailsTot += 1
    print 'Attempt #' + str(toss) + ": Throwing a coin... It's a " + result + '! ... Got ' + \
    str(headsTot) + ' head(s) so far and ' + str(tailsTot) + ' tail(s) so far'
  print 'Ending the program, thank you!'

coinToss()