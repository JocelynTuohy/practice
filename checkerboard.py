half_size = 4

for each in range(1,(half_size * 2) + 1):
    if each % 2 != 0:
        print ('* ') * half_size
    else:
        print (' *') * half_size
