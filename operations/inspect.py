import numpy as np

class Inspect:
    def __init__(self, arr):
        self.arr=arr
        
    # Data Type 
    def d_type(self):
        try:
            return f"The Data Type is: {self.arr.dtype}"
        except Exception as e:
            return f"Error while finding Data Type: {e}"
       
    # Dimension 
    def dimension(self):
        try:
            return f"The Dimension is: {self.arr.ndim}"
        except Exception as e:
            return f"Error while finding Dimension: {e}"
        
    # Length 
    def length(self):
        try:
            return f"The Length is: {len(self.arr)}"
        except Exception as e:
            return f"Error while finding Length: {e}"
        
    # Shape 
    def shape(self):
        try:
            return f"The Shape is: {self.arr.shape}"
        except Exception as e:
            return f"Error while finding Shape: {e}"
        
    # Size 
    def size(self):
        try:
            return f"The Size is: {self.arr.size}"
        except Exception as e:
            return f"Error while finding Size: {e}"
        
    # Summary
    def summary(self):
        try:
            return {
                "Data Type":self.arr.dtype,
                "Dimension":self.arr.ndim,
                "Length":len(self.arr),
                "Shape":self.arr.shape,
                "Size":self.arr.size,
            }
        except as Exception as e:
            return {"Error": str(e)}
        
        