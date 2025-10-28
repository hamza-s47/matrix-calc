import numpy as np

class Inspect:
    def __init__(self, arr):
        self.arr=np.array(arr)
        
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
        except Exception as e:
            return {"Error": str(e)}
        
    # Data Type 
    def d_type(self):
        try:
            return f"Data Type: {self.summary()['Data Type']}"
        except Exception as e:
            return f"Error while finding Data Type: {e}"
       
    # Dimension 
    def dimension(self):
        try:
            return f"Dimension: {self.summary()['Dimension']}"
        except Exception as e:
            return f"Error while finding Dimension: {e}"
        
    # Length 
    def length(self):
        try:
            return f"Length: {self.summary()['Length']}"
        except Exception as e:
            return f"Error while finding Length: {e}"
        
    # Shape 
    def shape(self):
        try:
            return f"Shape: {self.summary()['Shape']}"
        except Exception as e:
            return f"Error while finding Shape: {e}"
        
    # Size 
    def size(self):
        try:
            return f"Size: {self.summary()['Size']}"
        except Exception as e:
            return f"Error while finding Size: {e}"
        
    
        
        