import numpy as np
from colorama import Fore, Back, Style, init
import operations.arithmetic as ar
import operations.aggregate as ag

mat1=np.array([[1,2], [3,4]])
mat2=np.array([[6,3], [7,8]])
vect=np.array([1,2])

# print(vect.ndim)
# print(np.matmul(mat1, mat2))

# print(ar.addition(mat1, mat2))

# print(mat1+vect)

abc=ar.MatrixArithmetic(mat1, mat2)
agg=ag.Aggregate(mat1)
# print(agg.std_dev("s", "row"))

print (np.linspace(0,9, 3))