originalList = ['x',1,2,3,4,5,6,7,8,9,10,11,12]
for val in range(0,len(originalList)):
  printString = str(originalList[val]) + ' '
  for member in range(1,len(originalList)):
    if val == 0:
      printString = printString + str((val + 1) * originalList[member]) + ' '
    else:
      printString = printString + str(val * originalList[member]) + ' '
  print printString