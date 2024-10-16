import numpy as np
import math
import cmath

a = -3.0
z = -1.0 + 2.0j

print('a = ', a)
print('z = ', z)


#print('np.sqrt(a) = ', np.sqrt(a))
print('np.sqrt(z) = ', np.sqrt(z))

print('math.sqrt(a) = ',math.sqrt(a))
print('cmath.sqrt(z) = ', cmath.sqrt(z))


c = np.sqrt(a)
w = np.sqrt(z)

print('(np.sqrt(a))^2 = ', c**2)
print('(np.sqrt(z))^2 = ', w**2)

