import math
import numpy as np
from tktools import relerr

def maclaurin_exp(x,rtol,atol,max_deg):
    old_ret = 1.0
    ret = old_ret
    xn = 1.0
    coef = 1.0
    for i in range(1,max_deg):
        coef /= i
        xn *= x
        ret = old_ret + coef * xn
        if math.fabs(ret - old_ret) <= rtol * math.fabs(old_ret) + atol:
            return ret,i
        old_ret = ret
    return ret,i


def maclaurin_exp_m1(x,rtol,atol,max_deg):
    org_x = x
    x = math.fabs(x)
    int_x = math.floor(x)
    x = x - int_x

    old_ret = 1.0
    ret = old_ret
    xn = 1.0
    coef = 1.0
    for i in range(1,max_deg):
        coef /= i
        xn *= x
        ret = old_ret + coef*xn
        if math.fabs(ret - old_ret) <= rtol * math.fabs(old_ret) + atol:
            break
        old_ret = ret
    ret *= math.e ** int_x

    if org_x < 0:
        ret = 1 / ret
    return ret,i


rtol = 1.0e-10
atol = 1.0e-50
max_deg = 1000
x_array = np.linspace(-10,10,num=10)
maclaurin_val = [0,0]
deg = [0,0]
reldiff = [0,0]

print('     x    , relerr[0], relerr[1] ,deg[0], deg[1]')
for x in x_array:
    maclaurin_val[0],deg[0] = maclaurin_exp(x,rtol,atol,max_deg)
    maclaurin_val[1],deg[1] = maclaurin_exp_m1(x,rtol,atol,max_deg)
    math_val = math.exp(x)

    reldiff[0] = relerr(maclaurin_val[0],math_val)
    reldiff[1] = relerr(maclaurin_val[1],math_val)
    print(f'{x:10.3e},{reldiff[0]:10.3e},{reldiff[1]:10.3e},{deg[0]:5d},{deg[1]:5d}')

