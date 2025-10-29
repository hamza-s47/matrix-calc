import numpy as np

class Aggregate:
    def __init__(self, arr):
        self.arr=np.array(arr)
        
    # Correlation Coefficient
    def corr_coef(self, arr2):
        try:
            nArr2=np.array(arr2)
            if self.arr.ndim==1 and nArr2.ndim==1:
               return (np.corrcoef(self.arr, nArr2))[0,1]
            else:
                return (np.corrcoef(self.arr, nArr2, rowvar=False))
        except Exception as e:
            return(f"Error while finding Correlation Coefficient: {e}")
        
    # Commulative Product
    def cum_prod(self, ax):
        try:
            if ax in (0, 1, -1):
               return (np.cumprod(self.arr, axis=ax))
            else:
                raise ValueError("Invalid axis. Use '0' for Column-wise.")
        except Exception as e:
            return(f"Error while finding Commulative Product: {e}")
        
    # Cummulative Sum
    def cum_sum(self, ax):
        try:
            if ax in (0, 1, -1):
               return (np.cumsum(self.arr, axis=ax))
            else:
                raise ValueError("Invalid axis. Use '0' for Column-wise.")
        except Exception as e:
            return(f"Error while Finding Cumulative Sum: {e}")
        
    # Maximum
    def max(self, ax):
        try:
            if ax in (0, 1, -1):
               return (np.max(self.arr, axis=ax))
            else:
                raise ValueError("Invalid axis. Use '0' for Column-wise.")
        except Exception as e:
            return(f"Error while finding maximum value: {e}")
        
    # Mean
    def mean(self, ax):
        try:
            if ax in (0, 1, -1):
               return (np.mean(self.arr, axis=ax))
            else: 
                raise ValueError("Invalid axis. Use '0' for Column-wise.")
        except Exception as e:
            return(f"Error while finding Mean: {e}")
        
    # Median
    def median(self, ax):
        try:
            if ax in (0, 1, -1):
               return (np.median(self.arr, axis=ax))
            else:
                raise ValueError("Invalid axis. Use '0' for Column-wise.")
        except Exception as e:
            return(f"Error while finding Median: {e}")
    
    # Minimum
    def min(self, ax):
        try:
            if ax in (0, 1, -1):
               return (np.min(self.arr, axis=ax))
            else: 
                raise ValueError("Invalid axis. Use '0' for Column-wise.")
        except Exception as e:
            return(f"Error while finding minimum value: {e}")
        
    # Product of Element
    def prod(self, ax):
        try:
            if ax in (0, 1, -1):
               return (np.prod(self.arr, axis=ax))
            else: 
                raise ValueError("Invalid axis. Use '0' for Column-wise.")
        except Exception as e:
            return(f"Error while finding Product of Element: {e}")
        
    # Sum
    def sum(self, ax):
        try:
            if ax in (0, 1, -1):
               return (np.sum(self.arr, axis=ax))
            else: 
                raise ValueError("Invalid axis. Use '0' for Column-wise.")
        except Exception as e:
            return(f"Error while doing sum: {e}")
        
    # Variance
    def var(self, method, ax):
        if method in (0, 1):
            return self.__variance(method, ax)
        else:
            raise ValueError("Invalid method. Use '0' for population and '1' for sample.")
        
    # Standard Deviation
    def std_dev(self, method, ax):
        if method in (0, 1):
            return self.__sd(method, ax)
        else:
            raise ValueError("Invalid method. Use '0' for population and '1' for sample.")
      
      
    # (PRIVATE INSTANCES)
    # _variance_
    def __variance(self, delta, ax):
        try:
            if ax in (0, 1, -1):
                return (np.var(self.arr, axis=ax, ddof=delta))
            else:
                raise ValueError("Invalid axis. Use '0' for Column-wise.")
        except Exception as e:
            return(f"Error while finding Variance: {e}")
        
    # _standard deviation_
    def __sd(self, delta, ax):
        try:
            if ax in (0, 1, -1):
                return (np.std(self.arr, axis=ax, ddof=delta))
            else:
                raise ValueError("Invalid axis. Use '0' for Column-wise.")
        except Exception as e:
            return(f"Error while finding Standard Deviation: {e}")