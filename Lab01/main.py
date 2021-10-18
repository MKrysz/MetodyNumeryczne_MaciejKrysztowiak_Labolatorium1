import math
import numpy as np

def cylinder_area(r:float,h:float):
    #check whether input is valid
    if r <= 0 or h <= 0 or not isinstance(r, float)or not isinstance(h, float):
        return float('nan')
    return 2*math.pi*r*(r+h)

def fib(n:int):
    #check whether input is valid
    if n <= 0 or not isinstance(n ,int):
        return None

    a = 1.0
    b = 1.0
    result = []

    for i in range(n):
        result.append(a)
        c = a+b
        a = b
        b = c

    return np.array(result)

def matrix_calculations(a:float):

    M = np.array(
        ([a, 1, -a],
        [0 , 1, 1],
        [-a, a, 1]))
    Mt = np.transpose(M)
    Mdet = np.linalg.det(M)

    if Mdet == 0.0: #if an inverse matrix doesn't exist return nan 
        Minv = np.array("nan")
    else:
        Minv = np.linalg.inv(M)

    return Minv, Mt, Mdet

def custom_matrix(m:int, n:int):

    #check whether input is valid
    if not isinstance(m, int) or not isinstance(n, int):
        return None
    if m < 0 or n < 0:
        return None

    result = np.zeros((m, n))

    for row in range(m):
        for col in range(n):
            result[row, col] = col if col > row else row

    return result
