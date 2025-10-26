import numpy as np

class MatrixArithmetic:
    def __init__(self, arr1, arr2=None):
        self.arr1 = arr1
        self.arr2 = arr2

    
    # Addition
    def addition(self):
        try:
            return (self.arr1+self.arr2)
        except Exception as e:
            return (f"Error in Addition: {e}")

    # Subtraction
    def subtraction(self):
        try:
            return (self.arr1-self.arr2)
        except Exception as e:
            return (f"Error in Subtraction: {e}")

    # Element-wise Multiplication
    def multiplication(self):
        try:
            return (self.arr1*self.arr2)
        except Exception as e:
            return (f"Error in Element-wise Multiplication: {e}")
        
    # Division
    def division(self):
        try:
            inv_b = np.linalg.inv(self.arr2)
            return np.dot(self.arr1,inv_b)
        except Exception as e:
            return (f"Error in Division: {e}")
    
    # Dot Product
    def dot_product(self):
        try:
            if self.arr1.shape[1] == self.arr2.shape[0]:
                return (np.dot(self.arr1, self.arr2))
            else:
                raise ValueError(f"Shape mismatch: Array 1 shape: {self.arr1.shape}, Array 2 shape: {self.arr2.shape}")
        except Exception as e:
            return (f"Error in Dot Product: {e}")
        
    # Linear System
    def lin_sys(self):
        try:
            return np.linalg.solve(self.arr1, self.arr2)
        except Exception as e:
            return (f"Error in Solving Linear System: {e}")

    # Scalar Multiplication
    def s_multiplication(self, n):
        try:
            return (self.arr1*n)
        except Exception as e:
            return (f"Error in Scalar Multiplication: {e}")

    # Square Root
    def sqrt(self):
        try:
            if np.any(self.arr1<0):
                raise ValueError("Square root of negative numbers is not allowed.")
            return (np.sqrt(self.arr1))
        except Exception as e:
            return (f"Error in Square Root: {e}")
        
    # Sin
    def sin(self):
        try:
            return (np.sin(self.arr1))
        except Exception as e:
            return (f"Error in Sin: {e}")
        
    # Cos
    def cos(self):
        try:
            return (np.cos(self.arr1))
        except Exception as e:
            return (f"Error in Cos: {e}")
        
    # Log
    def log(self):
        try:
            if np.any(self.arr1 <= 0):
                raise ValueError("Logarithm undefined for Zero or Negative numbers.")
            return (np.log(self.arr1))
        except Exception as e:
            return (f"Error in Log: {e}")
        
    # Exponential
    def exp(self):
        try:
            result = np.exp(self.arr1)
            if np.any(np.isinf(result)):
                raise OverflowError("Overflow encountered in exponential.")
            return (result)
        except Exception as e:
            return (f"Error in Exp: {e}")