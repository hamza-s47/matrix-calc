import numpy as np

class MatrixArithmetic:
    def __init__(self, arr1, arr2=None):
        self.arr1 = arr1
        self.arr2 = arr2

    
    # Addition
    def addition(self):
        try:
            print (self.arr1+self.arr2)
        except Exception as e:
            print (f"Error in Addition: {e}")

    # Subtraction
    def subtraction(self):
        try:
            print (self.arr1-self.arr2)
        except Exception as e:
            print (f"Error in Subtraction: {e}")

    # Element-wise Multiplication
    def multiplication(self):
        try:
            print (self.arr1*self.arr2)
        except Exception as e:
            print (f"Error in Element-wise Multiplication: {e}")

    # Dot Product
    def dot_product(self):
        try:
            if self.arr1.shape[1] == self.arr2.shape[0]:
                print (np.dot(self.arr1, self.arr2))
            else:
                raise ValueError(f"Shape mismatch: Array 1 shape: {self.arr1.shape}, Array 2 shape: {self.arr2.shape}")
        except Exception as e:
            print (f"Error in Dot Product: {e}")

    # Scalar Multiplication
    def s_multiplication(self, n):
        try:
            print (self.arr1*n)
        except Exception as e:
            print (f"Error in Scalar Multiplication: {e}")

    # Square Root
    def sqrt(self):
        try:
            if np.any(self.arr1<0)
                raise ValueError("Square root of negative numbers is not allowed.")
            print (np.sqrt(self.arr1))
        except Exception as e:
            print (f"Error in Square Root: {e}")
        
    # Sin
    def sin(self):
        try:
            print (np.sin(self.arr1))
        except Exception as e:
            print (f"Error in Sin: {e}")
        
    # Cos
    def cos(self):
        try:
            print (np.cos(self.arr1))
        except Exception as e:
            print (f"Error in Cos: {e}")
        
    # Log
    def log(self):
        try:
            if np.any(self.arr1 <= 0):
                raise ValueError("Logarithm undefined for Zero or Negative numbers.")
            print (np.log(self.arr1))
        except Exception as e:
            print (f"Error in Log: {e}")
        
    # Exponential
    def exp(self):
        try:
            result = np.exp(self.arr1)
            if np.any(np.isinf(result)):
                raise OverflowError("Overflow encountered in exponential.")
            print (result)
        except Exception as e:
            print (f"Error in Exp: {e}")