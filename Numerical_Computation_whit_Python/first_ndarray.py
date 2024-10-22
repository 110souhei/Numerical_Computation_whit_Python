import numpy as np
import scipy.linalg as sclinalg

vec_a = np.array([1,2,1])
vec_b = np.array([-3,-2,-1])

print('vec_a = ', vec_a)
print('vec_b = ', vec_b)

vec_c = 3*vec_a + vec_b
print('vec_c = ', vec_c)

print('||vec_a||_2 = ',np.linalg.norm(vec_a))
print('||vec_a||_2 = ',sclinalg.norm(vec_a))


print('||vec_a||_1 = ',np.linalg.norm(vec_a,1))
print('||vec_a||_1 = ',sclinalg.norm(vec_a,1))


print('||vec_a||_inf = ',np.linalg.norm(vec_a,np.inf))
print('||vec_a||_inf = ',sclinalg.norm(vec_a,np.inf))