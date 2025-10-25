import numpy as np

class Manipulate:
    def __init__(self, arr):
        self.arr=arr
        
    def flatten(self):
        try:
            return self.arr.flatten()
        except Exception as e:
            return f"Error while Flattening: {e}"
        
    def ravel(self):
        try:
            return self.arr.ravel()
        except Exception as e:
            return f"Error while Raveling: {e}"
        
    def sorting(self, axis=None):
        try:
            if axis in (None, "row", "r"):
                return np.sort(self.arr, axis=-1)
            elif axis in ("col", "c"):
                return np.sort(self.arr, axis=0)
            else:
                raise ValueError("Invalid axis value, use 'row', 'col', or nothing")
        except Exception as e:
            return f"Error while Sorting: {e}"
        
    def transpose(self):
        try:
            return self.arr.T
        except Exception as e:
            return f"Error while Transposing: {e}"