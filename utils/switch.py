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

# AGGREGATE
def Aggregate(key, arr, arr2=None, axis=None, method=1):
    agg=aggregate.Aggregate(arr)
    
    agg_dict={
        "corr_coef":agg.corr_coef(arr2),
        "cum_prod":agg.cum_prod(axis),
        "cum_sum":agg.cum_sum(axis),
        "max":agg.max(axis),
        "mean":agg.mean(axis),
        "median":agg.median(axis),
        "min":agg.min(axis),
        "prod":agg.prod(axis),
        "sum":agg.min(axis),
        "var":agg.var(method, axis),
        "std":agg.std_dev(method, axis),
    }
    return agg_dict.get(key, f"'{key}' does not exist.")

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

# FILE MANAGEMENT
def file_sys(key, fileName, arr=None, d=None):
    fileSys=files.FileSystem()
    
    fileSys_dict={
        "loadNpy":lambda: fileSys.load_npy(fileName),
        "saveNpy":lambda: fileSys.save_npy(fileName, arr) if arr is not None else "No array provided.",
        "loadTxt":lambda: fileSys.load_txt(fileName, d),
        "saveTxt":lambda: fileSys.save_txt(fileName, arr, " " if d is None else d) if arr is not None else "No array provided."
    }
    func = fileSys_dict.get(key)
    if func is None:
        return f"'{key}' does not exist."
    return func()

# INIT
def Init(key, row=None, col=None, k=None, dt=None, l=0, h=100):
    initialize=init.Init()
    
    init_dict={
        "ones":initialize.ones(row, col, dt),
        "constants":initialize.constants(k, row, col, dt),
        "eye":initialize.eye_matrix(row, col, k, dt),
        # "idty_matrix":initialize.idty_matrix(k, dt),
        "linspace":initialize.linspace(row, col, k, dt),
        "random":initialize.random(row, col, dt, l, h),
        "arr_range":initialize.arr_range(row, col, k, dt),
        "zeros":initialize.zeros(row, col, dt)
    }
    return init_dict.get(key, f"'{key}' does not exist.")

# MANIPULATE
def Manip(key, arr, axis=None):
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