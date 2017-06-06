# Fun with Functions Assignment (Coding Dojo)

# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your
# program print the number of that iteration and specify whether it's an odd or even number.
def odd_even():
  for num in range(1,2001):
    if num % 2 == 0:
      print 'Number is ' + str(num) + '. This is an even number.'
    else:
      print 'Number is ' + str(num) + '. This is an odd number.'

# call my function
odd_even()

# Multiply
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4,
# 10, 16]) and returns a list where each value has been multiplied by 5.
def multiply(array,factor):
  newArray = []
  for index in range(0,len(array)):
    newArray.append(array[index] * factor)
  return newArray

# call my function
b = multiply([2,4,10,16],5)
print b

# Hacker Challenge
# Write a function that takes the multiply function call as an argument. Your new function should
# return the multiplied list as a two-dimensional list. Each internal list should contain the number
# of 1's as the number in the original list.
def layered_multiples(arr):
  new_array = []
  for index in range(0,len(arr)):
    new_array.append([])
    for index2 in range(0,arr[index]):
      new_array[index].append(1)
  return new_array

x = layered_multiples(multiply([2,4,5],3))
print x