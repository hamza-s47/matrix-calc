import utils.switch as methods
from colorama import Fore, Back, Style, init
import numpy as np

mat1=[[1,2], [3,4]]
mat2=[[6,9], [7,8]]
vect=[1,2,4,3,7,5]
n=3


print(methods.Aggregate("var", mat2, method=0))
print("\n")
# for key, val in methods.Inspect("summary", mat1).items():
#     print(f"{key}: {val}")

abc=np.array([[6,9], [7,8]])
print(np.sum(abc))