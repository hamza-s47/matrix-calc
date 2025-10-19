import numpy as np

# Addition
def addition(arr1, arr2):
    try:
        if arr1.shape == arr2.shape:
            return(arr1+arr2)
        else:
            raise ValueError("Shape of Array not matched!")
    except Exception as e:
        return f"Error in addition: {e}"