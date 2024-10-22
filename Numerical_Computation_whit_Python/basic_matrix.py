import numpy as np
import scipy.linalg as sclinalg
mat_a = np.array([[1,2,3],[2,2,2],[3,3,3]])
print('A = \n',mat_a)
mat_b = np.array([[-3,-3,-3],[-3,-2,-2],[-3,-2,-1]])
print('B = \n', mat_b)

vec_x = np.array([1,2,3])
print('x = ', vec_x)

mat_ax = mat_a.dot(vec_x)
print('Ax = ',mat_ax)

mat_3am4b = 3*mat_a - 4*mat_b
print('3A - 4B = \n',mat_3am4b)

mat_ab = mat_a.dot(mat_b)
print('A * B = \n',mat_ab)
mat_ab_at = mat_a @ mat_b
print('A @ B = \n', mat_ab_at)

print('||mat_a||_2 = ', np.linalg.norm(mat_a))
print('||mat_a||_2 = ', sclinalg.norm(mat_a))

print('||mat_a||_1 = ', np.linalg.norm(mat_a,1))
print('||mat_a||_1 = ', sclinalg.norm(mat_a,1))

print('||mat_a||_inf = ',np.linalg.norm(mat_a,np.inf))
print('||mat_a||_inf = ',sclinalg.norm(mat_a,np.inf))

print('||mat_a||_fro = ',np.linalg.norm(mat_a, "fro"))
print('||mat_a||_fro =',sclinalg.norm(mat_a,"fro"))