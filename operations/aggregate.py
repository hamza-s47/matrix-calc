import numpy as np

class Aggregate:
    def __init__(self, arr, axis=None):
        self.arr=arr
        self.axis=axis
        
        
    # Sum
    def sum(self):
        try:
            if self.axis is None:
               print (np.sum(self.arr))
            else:
                axis_str=self.axis.lower()
                if axis_str=="col":
                    print (np.sum(self.arr, axis=0))
                elif axis_str=="row":
                    print (np.sum(self.arr, axis=1))
                else: 
                    raise ValueError("Invalid axis. Use 'col' or 'row'.")
        except Exception as e:
            print(f"Error while doing sum: {e}")