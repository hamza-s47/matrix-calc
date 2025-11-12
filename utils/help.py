from colorama import Fore, Back, Style, init

help_commands={
    # ADVANCE
    # (Determinant)
    "det":f"""To find Determinant use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} det [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL} """,
    # (Inverse)
    "inv":f"""To find Inverse use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} inv [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL} """,
    # (Magnitude)
    "magnitude":f"""To find Magnitude use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} magnitude [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL} """,
    # (Rank)
    "rank":f"""To find Rank use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} rank [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL} """,
    # (Trace)
    "trace":f"""To find Trace use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} trace [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL} """,
    
    # AGGREGATE
    # (Correlation Coefficint)
    "corr_coef":f"""To find Correlation Coeficient use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} corr_coef [[1,2], [3,4],...,[n,n,...,n]] [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}
        matrix 1 -> [[1,2], [3,4],...,[n,n,...,n]]
        matrix 2 -> [[5,6], [7,8],...,[n,n,...,n]]""",
    # (Cummulative Product)
    "cum_prod":f"""To find Commulative Product use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} cum_prod [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}
        matrix -> [[1,2], [3,4],...,[n,n,...,n]]
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} cum_prod [[1,2], [3,4],...,[n,n,...,n]] 0 {Style.RESET_ALL}
        0 for column-wise (optional)
        1 for row-wise (optional)""",
    # (Max)
    "max":f"""To find Maximum value use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} max [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}
        matrix -> [[1,2], [3,4],...,[n,n,...,n]]
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} max [[1,2], [3,4],...,[n,n,...,n]] 0 {Style.RESET_ALL}
        0 for column-wise (optional)
        1 for row-wise (optional)""",
    # (Mean)
    "mean":f"""To find Mean use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} mean [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}
        matrix -> [[1,2], [3,4],...,[n,n,...,n]]
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} mean [[1,2], [3,4],...,[n,n,...,n]] 0 {Style.RESET_ALL}
        0 for column-wise (optional)
        1 for row-wise (optional)""",
    # (Median)
    "median":f"""To find Median use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} median [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}
        matrix -> [[1,2], [3,4],...,[n,n,...,n]]
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} median [[1,2], [3,4],...,[n,n,...,n]] 0 {Style.RESET_ALL}
        0 for column-wise (optional)
        1 for row-wise (optional)""",
    # (Product of Element)
    "prod":f"""To find Product of Element use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} prod [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}
        matrix -> [[1,2], [3,4],...,[n,n,...,n]]
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} prod [[1,2], [3,4],...,[n,n,...,n]] 0 {Style.RESET_ALL}
        0 for column-wise (optional)
        1 for row-wise (optional)""",
    # (Sum)
    "sum":f"""To find Sum use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} sum [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}
        matrix -> [[1,2], [3,4],...,[n,n,...,n]]
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} sum [[1,2], [3,4],...,[n,n,...,n]] 0 {Style.RESET_ALL}
        0 for column-wise (optional)
        1 for row-wise (optional)""",
    # (Standard Deviation)
    "std":f"""To find Standard Deviation use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} std [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}
        1) matrix -> [[1,2], [3,4],...,[n,n,...,n]]
        2) method -> 0 for Poppulation and 1 for Sample (Optional, Default=1)
        3) axis -> 0 for column-wise and 1 for row-wise (Optional)
        If use method and axis both then {Fore.WHITE+Back.YELLOW+Style.BRIGHT}[matrix] (method) (axis){Style.RESET_ALL}, if use axis then you have to give method explicitly:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} std [[1,2], [3,4],...,[n,n,...,n]] 0 1 {Style.RESET_ALL}""",
    # (Variance)
    "var":f"""To find Variance use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} var [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}
        1) matrix -> [[1,2], [3,4],...,[n,n,...,n]]
        2) method -> 0 for Poppulation and 1 for Sample (Optional, Default=1)
        3) axis -> 0 for column-wise and 1 for row-wise (Optional)
        If use method and axis both then {Fore.WHITE+Back.YELLOW+Style.BRIGHT}[matrix] (method) (axis){Style.RESET_ALL}, if use axis then you have to give method explicitly:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} var [[1,2], [3,4],...,[n,n,...,n]] 0 1 {Style.RESET_ALL}""",
    
    # ARITHMETIC
    # (Addition)
    "add":f"""To perform Matrix Addition use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} add [[1,2], [3,4],...,[n,n]] [[5,6], [7,8],...,[n,n]] {Style.RESET_ALL}
        matrix 1 -> [[1,2], [3,4],...,[n,n]]
        matrix 2 -> [[5,6], [7,8],...,[n,n]]""",
    # (Division)
    "divide":f"""To perform Matrix Division use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} divide [[1,2], [3,4],...,[n,n]] [[5,6], [7,8],...,[n,n]] {Style.RESET_ALL}
        matrix 1 -> [[1,2], [3,4],...,[n,n]]
        matrix 2 -> [[5,6], [7,8],...,[n,n]]""",
    # (Dot Product)
    "dot":f"""To find Dot Product use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} dot [[1,2], [3,4],...,[n,n]] [[5,6], [7,8],...,[n,n]] {Style.RESET_ALL}
        matrix 1 -> [[1,2], [3,4],...,[n,n]]
        matrix 2 -> [[5,6], [7,8],...,[n,n]]""",
    # (Element-wise Multiplication)
    "elementMul":f"""To perform Element-wise Multiplication use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} elementMul [[1,2], [3,4],...,[n,n]] [[5,6], [7,8],...,[n,n]] {Style.RESET_ALL}
        matrix 1 -> [[1,2], [3,4],...,[n,n]]
        matrix 2 -> [[5,6], [7,8],...,[n,n]]""",
    # (Linear System)
    "linear":f"""To find Linear System use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} linear [[1,2], [3,4],...,[n,n]] [[5,6], [7,8],...,[n,n]] {Style.RESET_ALL}
        matrix 1 -> [[1,2], [3,4],...,[n,n]]
        matrix 2 -> [[5,6], [7,8],...,[n,n]]""",
    # (Subtraction)
    "subtract":f"""To perform Matrix Subtraction use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} subtract [[1,2], [3,4],...,[n,n]] [[5,6], [7,8],...,[n,n]] {Style.RESET_ALL}
        matrix 1 -> [[1,2], [3,4],...,[n,n]]
        matrix 2 -> [[5,6], [7,8],...,[n,n]]""",
        
    # FILE MANAGEMENT
    # (Load npy)
    "loadNpy":f"""To load your .npy file use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} loadNpy into/your_file.npy {Style.RESET_ALL}""",
    # (Save npy)
    "saveNpy":f"""To save your Matrix data into .npy file use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} saveNpy destination/your_file [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}""",
    # (Load txt)
    "loadTxt":f"""To load your .txt file use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} loadTxt into/your_file.txt {Style.RESET_ALL}
    if use delimeter (in this case it is '_')
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} loadTxt into/your_file.txt _ {Style.RESET_ALL}""",
    # (Save txt)
    "saveTxt":f"""To save your Matrix data into .txt file use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} saveTxt destination/your_file.txt {Style.RESET_ALL}
    if use delimeter (in this case it is ',')
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} saveTxt destination/your_file.txt , {Style.RESET_ALL}""",
    
    # MANIPULATE
    # (Flatten)
    "flatten":f"""To Flatten the Matrix use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} flatten [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}""",
    # (Ravel)
    "ravel":f"""Ravel the Matrix use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} ravel [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}""",
    # (Sort)
    "sort":f"""To Sort the Matrix use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} sort [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}
        matrix -> [[1,2], [3,4],...,[n,n,...,n]]
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} sort [[1,2], [3,4],...,[n,n,...,n]] 0 {Style.RESET_ALL}
        0 for column-wise (optional)
        1 for row-wise (optional)""",
    # (Transpose)
    "transpose":f"""To Transpose the Matrix use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} transpose [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}""",
    
    # INSPECT
    # (Array Range)
    "arr_range":f"""To initialize the Vector of Range:
    Range Vector (in this case its 0 t0 4)
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} arr_range 5 {Style.RESET_ALL}
    Range Vector (in this case its 2 to 8) {Fore.YELLOW+Style.BRIGHT}(optional){Style.RESET_ALL}
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} arr_range 2 9 {Style.RESET_ALL}
    Range Vector (in this case 2,4,6,8)
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} arr_range 2 9 2 {Style.RESET_ALL}
    Default data type is {Fore.WHITE+Back.YELLOW+Style.BRIGHT}integer{Style.RESET_ALL}, use {Fore.WHITE+Back.YELLOW+Style.BRIGHT}decimal{Style.RESET_ALL} or {Fore.WHITE+Back.YELLOW+Style.BRIGHT}float{Style.RESET_ALL} for float data type
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} arr_range 2 9 2 float {Style.RESET_ALL}""",
    # (Constants)
    "constants":f"""To initialize the Matrix of Constants:
    Square Matrix (in this case its 3x3 of 9)
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} constants 9 3 {Style.RESET_ALL}
    Matrix (in this case its 2x4 of 5)
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} constants 5 2 4 {Style.RESET_ALL}
    Default data type is {Fore.WHITE+Back.YELLOW+Style.BRIGHT}integer{Style.RESET_ALL}, use {Fore.WHITE+Back.YELLOW+Style.BRIGHT}decimal{Style.RESET_ALL} or {Fore.WHITE+Back.YELLOW+Style.BRIGHT}float{Style.RESET_ALL} for float data type
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} constants 5 2 4 float {Style.RESET_ALL}""",
    # (Eye)
    "eye":f"""To initialize the Identity Matrix:
    Square Identity Matrix (in this case 3x3)
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} eye 3 {Style.RESET_ALL}
    Identity Matrix (in this case 2x4)
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} eye 2 4 {Style.RESET_ALL}
    Identity Matrix (in this case 2x4 and k=1, By default k=0)
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} eye 2 4 1 {Style.RESET_ALL}
    Default data type is {Fore.WHITE+Back.YELLOW+Style.BRIGHT}integer{Style.RESET_ALL}, use {Fore.WHITE+Back.YELLOW+Style.BRIGHT}decimal{Style.RESET_ALL} or {Fore.WHITE+Back.YELLOW+Style.BRIGHT}float{Style.RESET_ALL} for float data type
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} eye 2 4 1 float {Style.RESET_ALL}""",
    # (Linspace)
    "linspace":f"""To initialize the Linspace Matrix:
    Linspace Matrix (in this case from 3 to 5)
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} linspace 3 5 {Style.RESET_ALL}
    Linspace Matrix (in this case from 3 to 5 and 4 steps)
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} linspace 3 5 4 {Style.RESET_ALL}
    Default data type is {Fore.WHITE+Back.YELLOW+Style.BRIGHT}float{Style.RESET_ALL}, use {Fore.WHITE+Back.YELLOW+Style.BRIGHT}integer{Style.RESET_ALL} or {Fore.WHITE+Back.YELLOW+Style.BRIGHT}int{Style.RESET_ALL} for integer data type
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} linspace 3 5 4 int {Style.RESET_ALL}""",
    # (Ones)
    "ones":f"""To initialize the Matrix of Ones:
    Square Matrix (in this case 3x3)
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} ones 3 {Style.RESET_ALL}
    Matrix (in this case 2x4)
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} ones 2 4 {Style.RESET_ALL}
    Default data type is {Fore.WHITE+Back.YELLOW+Style.BRIGHT}integer{Style.RESET_ALL}, use {Fore.WHITE+Back.YELLOW+Style.BRIGHT}decimal{Style.RESET_ALL} or {Fore.WHITE+Back.YELLOW+Style.BRIGHT}float{Style.RESET_ALL} for float data type
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} ones 2 4 float {Style.RESET_ALL}""",
    # (Zeros)
    "zeros":f"""To initialize the Matrix of Zeros:
    Square Matrix (in this case 3x3)
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} zeros 3 {Style.RESET_ALL}
    Matrix (in this case 2x4)
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} zeros 2 4 {Style.RESET_ALL}
    Default data type is {Fore.WHITE+Back.YELLOW+Style.BRIGHT}integer{Style.RESET_ALL}, use {Fore.WHITE+Back.YELLOW+Style.BRIGHT}decimal{Style.RESET_ALL} or {Fore.WHITE+Back.YELLOW+Style.BRIGHT}float{Style.RESET_ALL} for float data type
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} zeros 2 4 float {Style.RESET_ALL}""",
    
    # INSPECT
    # (Data Type)
    "dataType":f"""To check Data Type use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} dataType [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}""",
    # (Dimension)
    "dimension":f"""To check the Dimension of the matrix use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} dimension [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}""",
    # (Length)
    "length":f"""To check the Length of the matrix use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} length [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}""",
    # (Shape)
    "shape":f"""To check the Shape of the matrix use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} shape [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}""",
    # (Size)
    "size":f"""To check the Size of the matrix use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} size [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}""",
    # (Summary)
    "summary":f"""For Summary use:
    {Fore.YELLOW+Back.GREEN+Style.BRIGHT} summary [[1,2], [3,4],...,[n,n,...,n]] {Style.RESET_ALL}""",
}