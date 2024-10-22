import numpy as np
import scipy as sc
import scipy.linalg as sclinalg

str_dim = input('正方行列サイズ DIM = ')
dim = int(str_dim)

np.random.seed(20200529)
mat_a = np.random.rand(dim,dim)
print('A = \n',mat_a)

true_x = np.random.rand(dim)

P,L,U = sclinalg.lu(mat_a)

print('P = \n', P)
print('L = \n', L)
print('U = \n', U)

print('|| P*L* U - A|| == 0? ->', np.linalg.norm(P @ L @ U - mat_a)/np.linalg.norm(mat_a))

LU, pivot = sclinalg.lu_factor(mat_a)
print('Pivot = ', pivot)
print('Lu = ', LU)

b = mat_a @ true_x
x = sclinalg.lu_solve((LU,pivot),b)
print('x = ', x)
print(f'rE(x)')