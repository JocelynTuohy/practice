# Find and Replace
words = "It's thanksgiving day. It's my birthday, too!"
print words.find('day')
newWords = words.replace('day','month')
print newWords

# Min and Max
x = [2,54,-2,7,12,98]
y = [4,5,'thing',93,[2,2,2,2]]
print min(x), max(x)
print min(y), max(y)

# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
y = [4883]
print x[0], x[len(x)-1]
print y[0], y[len(y)-1]

# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
half = len(x)/2
x.insert(0,[])
for count in range(1,half+1):
  x[0].insert(count-1,x[1])
  x.pop(1)
print x

# New List 2nd Test
y = [32793,734,4539,23,-239852,-2398542]
y.sort()
half = len(y)/2
y.insert(0,[])
for count in range(1,half+1):
  y[0].insert(count-1,y[1])
  y.pop(1)
print y