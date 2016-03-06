from random import randint 

size = 7 
# 1 - 9 just so that monospace fonts look nice
min_dist = 1
max_dist = 9 

with open('out.inp', 'wb') as f:
  f.write(str(size) + '\n')
  for i in xrange(size):
    for j in xrange(size):
      f.write(str(randint(min_dist, max_dist) if i != j else 0) + ' ')
    f.write('\n')
