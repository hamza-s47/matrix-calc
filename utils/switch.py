from operations import advance, aggregate, arithmetic, files, init, inspect, manipulate

# ADVANCE
def Adv(key, arr):
    adv=advance.AdvanceOps(arr)
    
    adv_dict={
        "det":adv.det(),
        "inv":adv.inv(),
        "magnitude":adv.magnitude(),
        "rank":adv.rank(),
        "trace":adv.trace()
    }
    return adv_dict.get(key, f"'{key}' does not exist.")

# ARITHMETIC
def Arithmetic(key, arr1, arr2=None, k=None):
    arth=arithmetic.MatrixArithmetic(arr1, arr2)
    
    arth_dict={
        "add":arth.addition(),
        "divide":arth.division(),
        "elementMul":arth.multiplication(),
        "exponential":arth.exp(),
        "dot":arth.dot_product(),
        "linear":arth.lin_sys(),
        "sqrt":arth.sqrt(),
        "sin":arth.sin(),
        "cos":arth.cos(),
        "log":arth.log(),
        "scalarMul":arth.s_multiplication(k),
        "subtract":arth.subtraction(),
    }
    return arth_dict.get(key, f"'{key}' does not exist.")

# MANIPULATE
def Manip(key, arr, axis=-1):
    manp=manipulate.Manipulate(arr)
    
    manp_dict={
        "flatten":manp.flatten(),
        "ravel":manp.ravel(),
        "sort":manp.sorting(axis),
        "transpose":manp.transpose()
    }
    return manp_dict.get(key, f"'{key}' does not exist.")

# INSPECT
def Inspect(key, arr):
    ins=inspect.Inspect(arr)
    
    ins_dict={
        "dataType":ins.d_type(),
        "dimension":ins.dimension(),
        "length":ins.length(),
        "shape":ins.shape(),
        "size":ins.size(),
        "summary":ins.summary()
    }
    return ins_dict.get(key, f"'{key}' does not exist.")