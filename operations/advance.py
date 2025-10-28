import numpy as np

class AdvanceOps:
    def __init__(self, arr):
        self.arr=np.array(arr)
        
    # Determinant
    def det(self):
        try:
            return np.linalg.det(self.arr)
        except Exception as e:
            return f"Error while finding Determinant: {e}"
        
    # Inverse
    def inv(self):
        try:
            return np.linalg.inv(self.arr)
        except Exception as e:
            return f"Error while finding Inverse: {e}"
        
    # Magnitude
    def magnitude(self):
        try:
            return np.linalg.norm(self.arr)
        except Exception as e:
            return f"Error while finding Magnitude: {e}"
        
    # Rank
    def rank(self):
        try:
            return np.linalg.matrix_rank(self.arr)
        except Exception as e:
            return f"Error while finding Rank: {e}"
        
    # Trace
    def trace(self):
        try:
            return np.trace(self.arr)
        except Exception as e:
            return f"Error while finding Trace: {e}"