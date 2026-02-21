# statistics = collection, organisation, displaying, analysing, interpreation and presentation of data
import numpy as np
import matplotlib.pyplot as plt

print(f"numpy: {np.__version__}")
# the available methods (modules) of numpy
# print(dir(np))

py_list = [1, 2, 3, 4, 5]
print(type(py_list))

py_two_d_list = [[0, 1, 2], [2, 3, 4], [6, 7, 8]]
print(type(py_two_d_list))

# numpy array
np_array = np.array(py_list)
np_two_d_list = np.array(py_two_d_list)
print(type(np_array))
print(type(np_two_d_list))

# float array 
np_array_float = np.array(py_list, dtype=float)
print(np_array_float)

np_bool_array = np.array([0, -1, -1, 0], dtype=bool)
print(np_bool_array)

# coverting back to list
np_to_list = np_array.tolist()
print(type(np_to_list))

# tuple to numpy array
py_tuple = (1, 2, 3, 4, 5)
print(type(py_tuple))
np_tuple = np.array(py_tuple)
print(type(np_tuple))

# numpy shape array
print(np_array.shape)
print(np_two_d_list.shape)

print(np_array.dtype)
print(np_array_float.dtype)
print(np_bool_array.dtype)

# size = number of elements
print(np_array.size)
print(np_array_float.size)
print(np_bool_array.size)

# can do mathematical operations of numpy arrays
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
plus_ten = numpy_array_from_list + 10
print(plus_ten)
modulus_3 = numpy_array_from_list % 3
print(modulus_3)

# float to int
numpy_int_arr = np.array([1.0, 2.0, 3.0, 4.0], dtype = 'int')
print(numpy_int_arr)

two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
# this will get the first row = [1, 2, 3]
print(two_dimension_array[0])
# this will get the first columns
print(two_dimension_array[:,0])
# this will get the first two rows and first two columns
print(two_dimension_array[0:2, 0:2])
# this will reverse both the rows and columns
print(two_dimension_array[::-1,::-1])

# setting values
two_dimension_array[1, 1] = 44
print(two_dimension_array)

# zeros
numpy_zeros = np.zeros((3, 3), dtype=int, order='C')
print(numpy_zeros)
numpy_ones = np.ones((3, 3), dtype=int, order='C')
print(numpy_ones)

# reshaoping (rows, columns)
original_shape  = np.array([(1,2,3), (4,5,6)])
reshape = original_shape.reshape(3, 2)
print(reshape)
flattened = reshape.flatten()
print(flattened)

# [1, 2, 3] + [4, 5, 6] = [5, 7, 9]
# to appened need to use horizontal append
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
horizontal_append = np.hstack((np_list_one, np_list_two))
print(horizontal_append)
vertical_append = np.vstack((np_list_one, np_list_two))
print(vertical_append)

# random_numbers 
random_float = np.random.random()
print(random_float)
# array of 5 random numbers
print(np.random.random(5))
# random number between 0 amd 10
print(np.random.randint(0, 11))
# row of random numbers between 0 and 10
print(np.random.randint(0, 11, size=4))

# (mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
print(normal_array)

# matrix in numpy
matrix = np.matrix(np.ones((4,4), dtype=float))
print(matrix)

# change the third array
np.asarray(matrix)[2] = 2
print(matrix)

# list using an array (0, 11, 2)
lst = range(0, 11, 2)
print(list(lst))
np_list = np.arange(0, 11, 2)
print(np_list)

# sequence of numbers using linear space/log space
# e.g 10 numebers equally spaced out between 1 and 5
print(np.linspace(1.0, 5.0, num=10))
# not including the last value in the interval
print(np.linspace(1.0, 5.0, num=5, endpoint=False))

# logspace returns even spaced numbers on a log scale. logspace has the same parameters parameters 
print(np.logspace(2, 4.0, num=4))