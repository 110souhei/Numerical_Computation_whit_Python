import numpy as np

def horner_poly(x, coef):
    deg = len(coef)
    ret = coef[0]
    for i in range(0,deg - 1):
        ret = ret * x + coef[i+1]

    return ret


poly_coef = [-4.0, 3.0, -2.0, 1.0]
print('poly_coef = ', poly_coef)

p = np.poly1d(poly_coef)
print('p(x) = \n', p)

x = np.sqrt(3.0)
print('horner p (', x ,') = ',horner_poly(x,poly_coef))
print('Numpy p(',x ,') = ',p(x))