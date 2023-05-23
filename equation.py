import os
import numpy as np

A = np.array([[2, 4], [1, 3]])
b = np.array([3, 1]).T

if np.linalg.det(A) == 0:
    print('cannot calculate inverse matrix - determinant is 0')
    os.system('exit')

A_inv = np.linalg.inv(A)
x = A_inv @ b

print(A_inv)
print(x)