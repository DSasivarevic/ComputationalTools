import numpy as np
import itertools

class Assignment2:
  def transform_to_array(self, x, y):
    a = np.zeros(shape=(x,y))
    return np.array([np.append(a, np.array(line.rstrip('\n'))) for line in open('matrix.txt')])
     
  def binary_counter(self, N):
    return [''.join(i) for i in itertools.product('01', repeat=N)]
  
  def matrix_to_file(self, file, X):
    np.savetxt(file, X, delimiter=' ') 

c = Assignment2()

#-----------------------------------#
#Exercise 2.1
#-----------------------------------#

#A
a = c.transform_to_array(3, 3)
print type(a)
print type(a[0])

#B
X = np.empty([3, 3])
c.matrix_to_file("X.txt", X)

#-----------------------------------#
#Exercise 2.2
#-----------------------------------#

print c.binary_counter(3)
#-----------------------------------#
