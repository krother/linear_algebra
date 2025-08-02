
#
# vectors
#

import numpy as np

# create vectors
a = np.array([1, 2], dtype=np.float32)

# vector addition
a + b

# apples, bananas, cherries
fruit = np.array([3, 1, 50])
prices = np.array([1.0, 0.5, 0.05])

fruit * 2

fruit * prices

np.dot(fruit, prices)

# cross product, needs 3 dimensions
a = np.array([1, 2, 0])
b = np.array([2, 1, 0])
np.cross(a, b)

np.cross(a, a) # null vector if cannot be determined

#
# Matrices
#
M = np.random.randint(low=0, high=5, size=(3, 4))

M + 10
M * 5

# position-wise multiplication
B = np.arange(12).reshape((3, 4))
A * B

# dpt product
M.shape, prices.shape

np.dot(M, prices)  # fails
np.dot(prices, M)

M.transpose()


# inverse
from numpy.linalg import inv

A = np.array([[1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1]])

Ai = inv(A)
inv(B)  # does not work - matrix has to be square

C = np.ones((4, 4))
inv(C)  # not all matrices are invertible

np.dot(A, Ai)  # identity matrix
np.dot(Ai, A)


#
# Linear transformation
#
a = np.array([3, 1])

R = np.array([[0, 1], [-1, 0]])
a = np.dot(a, R)
a = np.dot(a, R)
a = np.dot(a, R)
a = np.dot(a, R)

# turn by 30 degrees
from math import sin, cos, radians

angle = radians(30)
R = np.array([[cos(angle), sin(angle)], [-sin(angle), cos(angle)]])
a = np.dot(a, R)

# stretch
STRETCH = np.array([[2, 0], [0, 2]])
np.dot(a, STRETCH)

SHEAR = np.array([[2, 5], [0, 2]])

#
# Norms and distances
#
a = np.array([3, 1])
b = np.array([1, -4])

np.sum((a - b) ** 2)
np.sum(np.abs(a - b))

# cosine from ipynb


#
# linear equation systems
#
shoppers = np.array([[3, 1, 50], [10, 10, 10], [2, 3, 4]])
shoppers.shape

bills = np.dot(shoppers, prices)
np.linalg.solve(shoppers, bills)
inv(shoppers)

shoppers = np.array([[3, 1, 0], [10, 10, 0], [2, 3, 0]])
bills = np.dot(shoppers, prices)
np.linalg.solve(shoppers, bills)
inv(shoppers)

shoppers = np.array([[3, 1, 50], [10, 10, 10], [20, 20, 20]])
inv(shoppers)