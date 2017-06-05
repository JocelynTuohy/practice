

for num in range (100,100001):
  prime = True
  square = False
  for testee in range(10,num/2):
    if testee * testee == num:
      square = True
  for testeeni in range(2,num):
    if num % testeeni == 0:
      prime = False
  if not(prime or square):
    print 'FooBar'
  elif prime:
    print 'Foo'
  elif square:
    print 'Bar'