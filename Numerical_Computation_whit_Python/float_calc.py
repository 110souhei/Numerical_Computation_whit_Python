
import math

a = input('a = ')

b = input('b = ')
a,b = float(a),float(b)

print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)

print('sqrt(a) = ', math.sqrt(a))

c = math.sqrt(b)

print('(sqrt(b))^2 = ', c ** 2)


print('exp(a) = ',math.exp(a))
print('sin(a) = ', math.sin(a))
print('cos(a) = ',math.cos(a))
print('tan(a) = ', math.tan(a))
print('log(a) = ', math.log(a))
print('log10(a) = ', math.log10(a))