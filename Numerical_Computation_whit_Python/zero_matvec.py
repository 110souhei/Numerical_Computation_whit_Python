import numpy as np

str_dim = input('正方行列size dim = ')
dim = int(str_dim)

zero_vector = np.zeros(dim)

zero_matrix = np.zeros((dim,dim))

unit_matrix = np.eye(dim)

print('0 = ', zero_vector)
print('0 = \n', zero_matrix)
print('I = \n', unit_matrix)

one_vector = np.ones(dim)
one_matrix = np.ones((dim, dim))

print('one_vector = ',one_vector)
print('one_matrix = \n', one_matrix)