import numpy as np
x = np.array([1/6,np.pi])
A = np.array([[np.exp(1),-np.log(3)],[-np.sqrt(2),2/3]])

print('x =',x)
print('A = ');print(A)

approx_x = np.array([1.667e-1,3.1416])
approx_A = np.array([[2.7183,-1.0986],[-1.4142,6.6667e-1]])

print('approx_x = ', approx_x)
print('approx_A = ');print(approx_A)

print(f'rE1(approx_x) = {np.linalg.norm(x-approx_x,1)/np.linalg.norm(x,1):10.1e}')
print(f'rE2(approx_x) = {np.linalg.norm(x-approx_x,2)/np.linalg.norm(x,2):10.1e}')
print(f'rEi(approx_x) = {np.linalg.norm(x-approx_x,np.inf)/np.linalg.norm(x,np.inf):10.1e}')


print(f'rE1(approx_A) = {np.linalg.norm(x-approx_A,1)/np.linalg.norm(A,1):10.1e}')
print(f'rE2(approx_A) = {np.linalg.norm(x-approx_A,2)/np.linalg.norm(A,2):10.1e}')
print(f'rEi(approx_A) = {np.linalg.norm(x-approx_A,np.inf)/np.linalg.norm(A,np.inf):10.1e}')