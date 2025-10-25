import numpy as np

class Aggregate:
    def __init__(self, arr):
        self.arr=arr
        
    # Correlation Coefficient
    def corr_coef(self, arr2):
        try:
            if self.arr.ndim==1 and arr2.ndim==1:
               return (np.corrcoef(self.arr, arr2))
            else:
                return (np.corrcoef(self.arr, arr2, rowvar=False))
        except Exception as e:
            return(f"Error while finding Correlation Coefficient: {e}")
        
    # Commulative Product
    def cum_prod(self, axis=None):
        try:
            if axis is None:
               return (np.cumprod(self.arr))
            else:
                axis_str=axis.lower()
                if axis_str=="col":
                    return (np.cumprod(self.arr, axis=0))
                elif axis_str=="row":
                    return (np.cumprod(self.arr, axis=1))
                else: 
                    raise ValueError("Invalid axis. Use 'col' or 'row'.")
        except Exception as e:
            return(f"Error while finding Commulative Product: {e}")
        
    # Cummulative Sum
    def cum_sum(self, axis=None):
        try:
            if axis is None:
               return (np.cumsum(self.arr))
            else:
                axis_str=axis.lower()
                if axis_str=="col":
                    return (np.cumsum(self.arr, axis=0))
                elif axis_str=="row":
                    return (np.cumsum(self.arr, axis=1))
                else: 
                    raise ValueError("Invalid axis. Use 'col' or 'row'.")
        except Exception as e:
            return(f"Error while Finding Cummulative Sum: {e}")
        
    # Maximum
    def max(self, axis=None):
        try:
            if axis is None:
               return (np.max(self.arr))
            else:
                axis_str=axis.lower()
                if axis_str=="col":
                    return (np.max(self.arr, axis=0))
                elif axis_str=="row":
                    return (np.max(self.arr, axis=1))
                else: 
                    raise ValueError("Invalid axis. Use 'col' or 'row'.")
        except Exception as e:
            return(f"Error while finding maximum value: {e}")
        
    # Mean
    def mean(self, axis=None):
        try:
            if axis is None:
               return (np.mean(self.arr))
            else:
                axis_str=axis.lower()
                if axis_str=="col":
                    return (np.mean(self.arr, axis=0))
                elif axis_str=="row":
                    return (np.mean(self.arr, axis=1))
                else: 
                    raise ValueError("Invalid axis. Use 'col' or 'row'.")
        except Exception as e:
            return(f"Error while finding Mean: {e}")
        
    # Median
    def median(self, axis=None):
        try:
            if axis is None:
               return (np.median(self.arr))
            else:
                axis_str=axis.lower()
                if axis_str=="col":
                    return (np.median(self.arr, axis=0))
                elif axis_str=="row":
                    return (np.median(self.arr, axis=1))
                else: 
                    raise ValueError("Invalid axis. Use 'col' or 'row'.")
        except Exception as e:
            return(f"Error while finding Median: {e}")
    
    # Minimum
    def min(self, axis=None):
        try:
            if axis is None:
               return (np.min(self.arr))
            else:
                axis_str=axis.lower()
                if axis_str=="col":
                    return (np.min(self.arr, axis=0))
                elif axis_str=="row":
                    return (np.min(self.arr, axis=1))
                else: 
                    raise ValueError("Invalid axis. Use 'col' or 'row'.")
        except Exception as e:
            return(f"Error while finding minimum value: {e}")
        
    # Product of Element
    def poe(self, axis=None):
        try:
            if axis is None:
               return (np.prod(self.arr))
            else:
                axis_str=axis.lower()
                if axis_str=="col":
                    return (np.prod(self.arr, axis=0))
                elif axis_str=="row":
                    return (np.prod(self.arr, axis=1))
                else: 
                    raise ValueError("Invalid axis. Use 'col' or 'row'.")
        except Exception as e:
            return(f"Error while finding Product of Element: {e}")
        
    # Commulative Product
    def cum_prod(self, axis=None):
        try:
            if axis is None:
               return (np.cumprod(self.arr))
            else:
                axis_str=axis.lower()
                if axis_str=="col":
                    return (np.cumprod(self.arr, axis=0))
                elif axis_str=="row":
                    return (np.cumprod(self.arr, axis=1))
                else: 
                    raise ValueError("Invalid axis. Use 'col' or 'row'.")
        except Exception as e:
            return(f"Error while finding Commulative Product: {e}")
    
    # Sum
    def sum(self, axis=None):
        try:
            if axis is None:
               return (np.sum(self.arr))
            else:
                axis_str=axis.lower()
                if axis_str=="col":
                    return (np.sum(self.arr, axis=0))
                elif axis_str=="row":
                    return (np.sum(self.arr, axis=1))
                else: 
                    raise ValueError("Invalid axis. Use 'col' or 'row'.")
        except Exception as e:
            return(f"Error while doing sum: {e}")
        
    # Variance
    def var(self, method, axis=None):
        method=method.lower()
        if method in ("p", "population"):
            return self.__variance(0, axis)
        elif method in ("s", "sample"):
            return self.__variance(1, axis)
        else:
            raise ValueError("Invalid method. Use 'p' for population and 's' for sample.")
        
    # Standard Deviation
    def std_dev(self, method, axis=None):
        method=method.lower()
        if method in ("p", "population"):
            return self.__sd(0, axis)
        elif method in ("s", "sample"):
            return self.__sd(1, axis)
        else:
            raise ValueError("Invalid method. Use 'p' for population and 's' for sample.")
      
      
    # (PRIVATE INSTANCES)
    # _variance_
    def __variance(self, delta, axis):
        try:
            if axis is None:
                return (np.var(self.arr, ddof=delta))
            else:
                axis_str=axis.lower()
                if axis_str=="col":
                    return (np.var(self.arr, axis=0, ddof=delta))
                elif axis_str=="row":
                    return (np.var(self.arr, axis=1, ddof=delta))
                else: 
                    raise ValueError("Invalid axis. Use 'col' or 'row'.")
        except Exception as e:
            return(f"Error while finding Variance: {e}")
        
    # _standard deviation_
    def __sd(self, delta, axis):
        try:
            if axis is None:
                return (np.std(self.arr, ddof=delta))
            else:
                axis_str=axis.lower()
                if axis_str=="col":
                    return (np.std(self.arr, axis=0, ddof=delta))
                elif axis_str=="row":
                    return (np.std(self.arr, axis=1, ddof=delta))
                else: 
                    raise ValueError("Invalid axis. Use 'col' or 'row'.")
        except Exception as e:
            return(f"Error while finding Standard Deviation: {e}")